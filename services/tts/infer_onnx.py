import numpy as np
import onnxruntime

from text import text_to_sequence, sequence_to_text
import torch
import gradio as gr
import soundfile as sf
import tempfile
import yaml
import json
import os

from time import perf_counter
import random

from AinaTheme import theme

from fastapi import FastAPI
from pydantic import BaseModel
import threading
import uvicorn



DEFAULT_SPEAKER_ID = os.environ.get("DEFAULT_SPEAKER_ID", default="quim")
DEFAULT_ACCENT= os.environ.get("DEFAULT_ACCENT", default="balear")

def intersperse(lst, item):
    result = [item] * (len(lst) * 2 + 1)
    result[1::2] = lst
    return result
 
    
def process_text(i: int, text: str, device: torch.device, cleaner:str):
    print(f"[{i}] - Input text: {text}")
    x = torch.tensor(
        intersperse(text_to_sequence(text, [cleaner]), 0),
        dtype=torch.long,
        device=device,
    )[None]
    x_lengths = torch.tensor([x.shape[-1]], dtype=torch.long, device=device)
    x_phones = sequence_to_text(x.squeeze(0).tolist())
    print(x_phones)
    return x.numpy(), x_lengths.numpy()

# paths
# MODEL_PATH_MATCHA_MEL_BAL="matcha_multispeaker_cat_bal_opset_15_10_steps.onnx"
# MODEL_PATH_MATCHA_MEL_CAT="matcha_multispeaker_cat_cen_opset_15_10_steps.onnx"
# MODEL_PATH_MATCHA_MEL_OCC="matcha_multispeaker_cat_occ_opset_15_10_steps.onnx"
# MODEL_PATH_MATCHA_MEL_VAL="matcha_multispeaker_cat_val_opset_15_10_steps.onnx"

MODEL_PATH_MATCHA_MEL_ALL="matcha_multispeaker_cat_all_opset_15_10_steps.onnx"

MODEL_PATH_VOCOS="mel_spec_22khz_cat.onnx"
CONFIG_PATH="config.yaml"
SPEAKER_ID_DICT="spk_to_id_3.json"

# Load models
sess_options = onnxruntime.SessionOptions()

# model_matcha_mel_bal = onnxruntime.InferenceSession(str(MODEL_PATH_MATCHA_MEL_BAL), sess_options=sess_options, providers=["CPUExecutionProvider"])
# model_matcha_mel_cat = onnxruntime.InferenceSession(str(MODEL_PATH_MATCHA_MEL_CAT), sess_options=sess_options, providers=["CPUExecutionProvider"])
# model_matcha_mel_occ = onnxruntime.InferenceSession(str(MODEL_PATH_MATCHA_MEL_OCC), sess_options=sess_options, providers=["CPUExecutionProvider"])
# model_matcha_mel_val = onnxruntime.InferenceSession(str(MODEL_PATH_MATCHA_MEL_VAL), sess_options=sess_options, providers=["CPUExecutionProvider"])

model_matcha_mel_all = onnxruntime.InferenceSession(str(MODEL_PATH_MATCHA_MEL_ALL), sess_options=sess_options, providers=["CPUExecutionProvider"])

model_vocos = onnxruntime.InferenceSession(str(MODEL_PATH_VOCOS), sess_options=sess_options, providers=["CPUExecutionProvider"])

speaker_id_dict = json.load(open(SPEAKER_ID_DICT))
accents = [e for e in speaker_id_dict.keys()]

# models={"balear":model_matcha_mel_bal,
#         "nord-occidental": model_matcha_mel_occ,
#         "valencia": model_matcha_mel_val,
#         "central": model_matcha_mel_cat}

cleaners={"balear": "catalan_balear_cleaners",
        "nord-occidental": "catalan_occidental_cleaners",
        "valencia": "catalan_valencia_cleaners",
        "central": "catalan_cleaners"}


speakers = [sp for sp in speaker_id_dict[DEFAULT_ACCENT].keys()]

def vocos_inference(mel,denoise):

    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)

    params = config["feature_extractor"]["init_args"]
    sample_rate = params["sample_rate"]
    n_fft= params["n_fft"]
    hop_length= params["hop_length"]
    win_length = n_fft

    # ONNX inference
    mag, x, y = model_vocos.run(
        None,
        {
            "mels": mel
        },
    )

    # complex spectrogram from vocos output
    spectrogram = mag * (x + 1j * y)
    window = torch.hann_window(win_length)

    if denoise:
        # Vocoder bias
        mel_rand = torch.zeros_like(torch.tensor(mel))
        mag_bias, x_bias, y_bias = model_vocos.run(
            None,
            {
                "mels": mel_rand.float().numpy()
            },
        )

        # complex spectrogram from vocos output
        spectrogram_bias = mag_bias * (x_bias + 1j * y_bias)

        # Denoising
        spec = torch.view_as_real(torch.tensor(spectrogram))
        # get magnitude of vocos spectrogram
        mag_spec = torch.sqrt(spec.pow(2).sum(-1))

        # get magnitude of bias spectrogram
        spec_bias = torch.view_as_real(torch.tensor(spectrogram_bias))
        mag_spec_bias = torch.sqrt(spec_bias.pow(2).sum(-1))

        # substract 
        strength = 0.0025
        mag_spec_denoised = mag_spec - mag_spec_bias * strength
        mag_spec_denoised = torch.clamp(mag_spec_denoised, 0.0)

        # return to complex spectrogram from magnitude
        angle = torch.atan2(spec[..., -1], spec[..., 0] )
        spectrogram = torch.complex(mag_spec_denoised * torch.cos(angle), mag_spec_denoised * torch.sin(angle))

    # Inverse stft
    pad = (win_length - hop_length) // 2
    spectrogram = torch.tensor(spectrogram)
    B, N, T = spectrogram.shape

    print("Spectrogram synthesized shape", spectrogram.shape)
    # Inverse FFT
    ifft = torch.fft.irfft(spectrogram, n_fft, dim=1, norm="backward")
    ifft = ifft * window[None, :, None]

    # Overlap and Add
    output_size = (T - 1) * hop_length + win_length
    y = torch.nn.functional.fold(
        ifft, output_size=(1, output_size), kernel_size=(1, win_length), stride=(1, hop_length),
    )[:, 0, 0, pad:-pad]

    # Window envelope
    window_sq = window.square().expand(1, T, -1).transpose(1, 2)
    window_envelope = torch.nn.functional.fold(
        window_sq, output_size=(1, output_size), kernel_size=(1, win_length), stride=(1, hop_length),
    ).squeeze()[pad:-pad]

    # Normalize
    assert (window_envelope > 1e-11).all()
    y = y / window_envelope
    
    return y


def tts(text:str, accent:str, spk_name:str, temperature:float, length_scale:float):
    if len(text) > 500:
        gr.Info("The maximum input allowed is 500 characters.")

    else:
        denoise=True
        spk_id = speaker_id_dict[accent][spk_name]
        sid = np.array([int(spk_id)]) if spk_id is not None else None
        text_matcha , text_lengths = process_text(0,text,"cpu",cleaner=cleaners[accent])
        # model_matcha_mel = models[accent]
        model_matcha_mel = model_matcha_mel_all

        # MATCHA VOCOS
        inputs = {
            "x": text_matcha,
            "x_lengths": text_lengths,
            "scales": np.array([temperature, length_scale], dtype=np.float32),
            "spks": sid
        }
        mel_t0 = perf_counter()
        # matcha mel inference
        mel, mel_lengths = model_matcha_mel.run(None, inputs)
        mel_infer_secs = perf_counter() - mel_t0
        print("Matcha Mel inference time", mel_infer_secs)

        vocos_t0 = perf_counter()
        # vocos inference
        wavs_vocos = vocos_inference(mel,denoise)
        vocos_infer_secs = perf_counter() - vocos_t0
        print("Vocos inference time", vocos_infer_secs)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False, dir="/home/user/app/data") as fp_matcha_vocos:
            sf.write(fp_matcha_vocos.name, wavs_vocos.squeeze(0), 22050, "PCM_24")

        print(f"RTF matcha + vocos { (mel_infer_secs + vocos_infer_secs) / (wavs_vocos.shape[1]/22050) }")
        print(f"Output file:{fp_matcha_vocos.name}")
        return fp_matcha_vocos.name


## GUI space

title = """
<div style="text-align: center; max-width: 700px; margin: 0 auto;">
    <div
        style="display: inline-flex; align-items: center; gap: 0.8rem; font-size: 1.75rem;"
    > <h1 style="font-weight: 900; margin-bottom: 7px; line-height: normal;">
        Natural and efficient TTS in Catalan
    </h1> </div>
</div>
 """

description = """
 
🍵 Matxa és un model TTS multilocutor multidialectal que utilitza 🥑  alVoCat com a vocoder. Es basen en arquitectures Matcha-TTS i Vocos.

Podeu provar les veus a continuació i saber els detalls tècnics a la pestanya "Informació".

----

🍵 Matxa is a multispeaker multidialect TTS model which uses 🥑 alVoCat as a vocoder. They are based on Matcha-TTS and Vocos architectures. 

You can synthesize test sentences below and check the technical details in the "About" tab.

"""

with open("about.md", "r", encoding="utf-8") as f:
    about = f.read()

with open("informacio.md", "r", encoding="utf-8") as f:
    informacio = f.read()

article = "Training and demo by The Language Technologies Unit from Barcelona Supercomputing Center."


def rs_change(accent):
    rnd_idx = random.randint(0, 1)
    return gr.Dropdown(choices=speaker_id_dict[accent], interactive=True,value=list(speaker_id_dict[accent].keys())[rnd_idx])

accent_dropdown = gr.Dropdown(
            choices=accents,
            label="Accent",
            value=DEFAULT_ACCENT,
            info=f"Models are trained on 4 accents"
        )

speaker_dropdown = gr.Dropdown(
            choices=speaker_id_dict[DEFAULT_ACCENT],
            label="Speaker id",
            value=DEFAULT_SPEAKER_ID,
            info=f"Models are trained on 2 speakers. You can prompt the model using one of these speaker ids.",  
            interactive=True   
        )

matcha_inference = gr.Interface(
    fn=tts,
    allow_flagging="never",
    inputs=[
        gr.Textbox(
            value="m'ha costat molt desenvolupar una veu, i ara que la tinc no estaré en silenci.",
            max_lines=1,
            label="Input text ",
            info="max 500 characters",
        ),
        accent_dropdown,
        speaker_dropdown,
        gr.Slider(
            0.1,
            0.8,
            value=0.2,
            step=0.01,
            label="Temperature",
            info=f"Temperature",
        ),
        gr.Slider(
            0.8,
            1.1,
            value=0.89,
            step=0.01,
            label="Length scale",
            info=f"Controls speech pace, larger values for slower pace and smaller values for faster pace",
        ),
    ],
    outputs=[gr.Audio(label="Matxa + alVoCat", interactive=False, type="filepath")]
)

about_tab = gr.Blocks()
with about_tab:
    gr.Markdown(about)
informacio_tab = gr.Blocks()
with informacio_tab:
    gr.Markdown(informacio)
demo = gr.Blocks(theme=theme, css="./styles.css")

# --- FastAPI app to run in a separate thread ---
app = FastAPI(title="local-aina-tts")

class SynthesizeRequest(BaseModel):
    text: str
    accent: str = DEFAULT_ACCENT
    spk_name: str = DEFAULT_SPEAKER_ID
    temperature: float = 0.2
    length_scale: float = 0.89

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/synthesize")
async def synthesize(req: SynthesizeRequest):
    # call existing tts() which returns a filepath
    out_path = tts(req.text, req.accent, req.spk_name, req.temperature, req.length_scale)
    return out_path

def _run_api():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

# start FastAPI in a daemon thread so Gradio can run in foreground
api_thread = threading.Thread(target=_run_api, daemon=True)
api_thread.start()

with demo:
    gr.Markdown(title)
    gr.Markdown(description)
    gr.TabbedInterface([matcha_inference, about_tab, informacio_tab], ["Demo", "About", "Informació"])
    accent_dropdown.select(fn=rs_change, inputs=accent_dropdown, outputs=speaker_dropdown)
    gr.Markdown(article)

demo.queue(max_size=10)
demo.launch(show_api=True, server_name="0.0.0.0", server_port=7860)
