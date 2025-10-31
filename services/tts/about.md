## 📄 About
Natural and efficient TTS in Catalan: 🍵+🥑

Here you can find all the information regarding our models 🍵 Matxa and 🥑 alVoCat, which have been trained with the use of deep learning. If you want specific information on how to train these model you can find it [here](https://huggingface.co/BSC-LT/matcha-tts-cat-multiaccent) and [here](https://huggingface.co/BSC-LT/vocos-mel-22khz-cat) respectively. The code we've used is also on Github [here](https://github.com/langtech-bsc/Matcha-TTS/tree/dev-cat).

## Table of Contents
<details>
<summary>Click to expand</summary>

- [General Model Description](#general-model-description)
- [Intended Uses and Limitations](#intended-uses-and-limitations)
- [Samples](#samples)
- [Main components](#main-components)
- [The model in detail](#the-model-in-detail)
- [Adaptation to Catalan](#adaptation-to-catalan)
- [Citation](#citation)  
- [Additional Information](#additional-information)

</details>

## General Model Description

The significance of open-source text-to-speech (TTS) technologies for minority languages cannot be overstated. These technologies democratize access to TTS solutions by providing a framework for communities to develop and adapt models according to their linguistic needs. This is why we have developed different open-source TTS solutions in Catalan, using an ensemble of technologies.

Here we present 🍵 Matxa, the first multispeaker, multidialectal neural TTS model. It comes together with the vocoder model 🥑 alVoCat, to generate high quality and expressive speech efficiently in four dialects:

* Balear
* Central
* North-Occidental
* Valencian

Both models are trained with open data; 🍵 Matxa models are free (as in freedom) to use for non-comercial purposes, but for commercial purposes it needs licensing from the voice artist. For details please consult the [License](#additional-information) section and the [model page](https://huggingface.co/BSC-LT/matcha-tts-cat-multiaccent/).


## Intended Uses and Limitations

This model is intended to serve as an acoustic feature generator for multispeaker text-to-speech systems for the Catalan language. 
It has been finetuned using a Catalan phonemizer, therefore if the model is used for other languages it may will not produce intelligible samples after mapping 
its output into a speech waveform. 

The quality of the samples can vary depending on the speaker. 
This may be due to the sensitivity of the model in learning specific frequencies and also due to the quality of samples for each speaker.

## Samples
* Female samples 
<div class="table-wrapper">
  <table class="tg">
    <thead>
      <tr>
        <th class="tg-0pky">Valencian</td>
        <th class="tg-0pky">Occidental</td>
        <th class="tg-0pky">Balear</td>
      <tr>
    <thead>
    <tbody>
      <tr>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk1/0.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk1/0.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk1/0.wav" type="audio/wav">
          </audio>
        </td>
      </tr>
      <tr>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk1/1.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk1/1.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk1/1.wav" type="audio/wav">
          </audio>
        </td>
      </tr>
      <tr>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk1/2.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk1/2.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk1/2.wav" type="audio/wav">
          </audio>
        </td>
      </tr>
    </tbody>
  </table>
</div>

* Male samples:

<div class="table-wrapper">
  <table class="tg">
    <thead>
      <tr>
        <th class="tg-0pky">Valencian</td>
        <th class="tg-0pky">Occidental</td>
        <th class="tg-0pky">Balear</td>
      <tr>
    <thead>
    <tbody>
      <tr>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk0/0.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk0/0.wav" type="audio/wav"">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk0/0.wav" type="audio/wav">
          </audio>
        </td>
      </tr>
      <tr>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk0/1.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk0/1.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk0/1.wav" type="audio/wav">
          </audio>
        </td>
      </tr>
      <tr>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/valencia/spk0/2.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/occidental/spk0/2.wav" type="audio/wav">
          </audio>
        </td>
        <td>
          <audio controls="" preload="none">
            audio not supported
            <source src="https://github.com/mllopartbsc/assets/raw/c6a393237e712851dd7cc7d10c70dde29d3412ac/matcha_tts_catalan/balear/spk0/2.wav" type="audio/wav">
          </audio>
        </td>
      </tr>
    </tbody>
  </table>
</div>

## Main components

Our text-to-speech model tailored for Catalan employs a multi-step process to convert written text into spoken words with accurate pronunciation. These are the steps:

1- Initially, the model analyzes the input text, breaking it down into smaller linguistic units such as words and sentences while identifying any special characters. It then utilizes our version of eSpeak, a speech phonemizer, to generate phonemes based on the Catalan language's phonetic rules. For each Catalan accent, certain specifically adapted eSpeak rules apply.

2- The matcha-TTS model converts these phonemes into a mel spectrogram, a visual representation of the spectrum of frequencies of a sound over time. 

3- This spectrogram is then fed into [our adaptation of the Vocos vocoder](https://huggingface.co/BSC-LT/vocos-mel-22khz-cat), which synthesizes the speech waveform.

By employing this series of steps, the TTS model ensures accurate pronunciation and natural-sounding Catalan speech output adapted to the nuances of the language. The computing of these steps was performed by Marenostrum 5 from the Barcelona Supercomputing Center, and Finisterrae III from CESGA.

Together, these technologies form a comprehensive TTS solution tailored to the needs of Catalan speakers, exemplifying the power of open-source initiatives in advancing linguistic diversity and inclusivity.


## The model in detail

**Matcha-TTS** is a non-autorregressive encoder-decoder model designed for fast acoustic modelling in TTS. 
The encoder part processes input sequences of phonemes and, together with a phoneme duration predictor, outputs averaged acoustic features. And the decoder,
which is essentially a U-Net backbone based on the Transfomer architecture, predicts the refined spectrogram.
The model is trained with optimal-transport conditional flow matching. 
This yields an ODE-based decoder capable of generating high output quality in fewer synthesis steps.

**Vocos** is a fast neural vocoder designed to synthesize audio waveforms from acoustic features. 
Unlike other typical GAN-based vocoders, Vocos does not model audio samples in the time domain. 
Instead, it generates spectral coefficients, facilitating rapid audio reconstruction through inverse Fourier transform.
The goal of this model is to provide an alternative to hifi-gan that is faster and compatible with the acoustic output of several TTS models. 
This version is tailored for the Catalan language, as it was trained only on Catalan speech datasets.

## Adaptation to Catalan

The original Matcha-TTS model excels in English, but to adapt it to Catalan, we have carried out a multi-stage process. 
First, we fine-tuned the English to Catalan model by creating a Matxa-base, using a 100h subset of the [CommonVoice](https://commonvoice.mozilla.org/es/datasets) v.16 Catalan database. 
The selection of this small set of samples has been performed automatically using the [UTMOS](https://arxiv.org/abs/2204.02152) system, a predictor of values of the metric Mean Opinion Score (MOS) a score usually set by human evaluators according to their subjective perception of speech quality.

Then we further fine-tuned the single accent Catalan Matxa-based model with the soon to be published LaFrescat dataset that has 3.5 hours of recordings for four dialectal variants:
  
 * Valencian
 
 * Occidental

 * Central

 * Balear 
 
With a male and a female speaker for each dialect.

Then, through fine-tuning for these specific Catalan dialects, the model adapted to regional variations in pronunciation and cadence. This meticulous approach ensures that the model reflects the linguistic richness and cultural diversity within the Catalan-speaking community, offering seamless communication in previously underserved dialects.
 
In addition to training the Matcha-TTS model for Catalan, integrating the eSpeak phonemizer played a crucial role in enhancing the naturalness and accuracy of generated speech. A TTS (Text-to-Speech) system comprises several components, each contributing to the overall quality of synthesized speech. The first component involves text preprocessing, where the input text undergoes normalization and linguistic analysis to identify words, punctuation, and linguistic features. Next, the text is converted into phonemes, the smallest units of sound in a language, through a process called phonemization. This step is where the eSpeak phonemizer shines, as it accurately converts Catalan text into phonetic representations, capturing the subtle nuances of pronunciation specific to Catalan. You can find the eSpeak version we used [here](https://github.com/projecte-aina/espeak-ng/tree/dev-ca).

After phonemization, the phonemes are passed to the synthesis component, where they are transformed into audible speech. Here, the Matcha-TTS model takes center stage, generating high-quality speech output based on the phonetic input. The model's training, fine-tuning, and adaptation to Catalan ensure that the synthesized speech retains the natural rhythm, intonation, and pronunciation patterns of the language, thereby enhancing the overall user experience.

Finally, the synthesized speech undergoes post-processing, where prosodic features such as pitch, duration, and emphasis are applied to further refine the output and make it sound more natural and expressive. By integrating the eSpeak phonemizer into the TTS pipeline and adapting it for Catalan, alongside training the Matcha-TTS model for the language, we have created a comprehensive and effective system for generating high-quality Catalan speech. This combination of advanced techniques and meticulous attention to linguistic detail is instrumental in bridging language barriers and facilitating communication for Catalan speakers worldwide.

## Citation

If this code contributes to your research, please cite the work:

```
@misc{LTU2024,
  title={Natural and efficient TTS in Catalan: using Matcha-TTS with the Catalan language},
  author={The Language Technologies Unit from Barcelona Supercomputing Center},
  year={2024},
}
```
```
@misc{mehta2024matchatts,
      title={Matcha-TTS: A fast TTS architecture with conditional flow matching}, 
      author={Shivam Mehta and Ruibo Tu and Jonas Beskow and Éva Székely and Gustav Eje Henter},
      year={2024},
      eprint={2309.03199},
      archivePrefix={arXiv},
      primaryClass={eess.AS}
}
```

## Additional Information

### Author
The Language Technologies Unit from Barcelona Supercomputing Center.

### Contact
For further information, please email <langtech@bsc.es>.

### Copyright
Copyright(c) 2023 by Language Technologies Unit, Barcelona Supercomputing Center.

### License
The demo page and the inference scripts are under [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

The model weights are licensed under [Creative Commons Attribution Non-commercial 4.0](https://www.creativecommons.org/licenses/by-nc/4.0/). These models are free to use for non-commercial and research purposes. Commercial use is only possible through licensing by
the voice artists. For further information, contact <langtech@bsc.es> and <lafrescaproduccions@gmail.com>. For more information see the [model page](https://huggingface.co/BSC-LT/matcha-tts-cat-multiaccent/).

### Funding
This work has been promoted and financed by the Generalitat de Catalunya through the [Aina project](https://projecteaina.cat/).

Part of the training of the model was possible thanks to the compute time given by Galician Supercomputing Center CESGA
([Centro de Supercomputación de Galicia](https://www.cesga.es/)), and also by [Barcelona Supercomputing Center](https://www.bsc.es/) in MareNostrum 5.