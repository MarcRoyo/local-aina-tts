import argparse
import requests
import sys

DEFAULT_URL = "http://localhost:8000/synthesize"

def synthesize(text, url=DEFAULT_URL, accent=None, spk_name=None,
               temperature=0.2, length_scale=0.89, out="output.wav", timeout=60):
    payload = {
        "text": text,
        "accent": accent or "",
        "spk_name": spk_name or "",
        "temperature": float(temperature),
        "length_scale": float(length_scale)
    }
    resp = requests.post(url, json=payload, timeout=timeout, stream=True)
    if resp.status_code == 200:
        # with open(out, "wb") as f:
        #     for chunk in resp.iter_content(chunk_size=8192):
        #         if chunk:
        #             f.write(chunk)
        print(f"Saved audio to {resp}")
        return 0
    else:
        print(f"Error {resp.status_code}: {resp.text}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Call local-aina-tts FastAPI synthesize endpoint")
    p.add_argument("text", help="Text to synthesize")
    p.add_argument("--url", default=DEFAULT_URL, help="FastAPI synthesize URL")
    p.add_argument("--accent", help="Accent id (optional)")
    p.add_argument("--spk", dest="spk_name", help="Speaker id (optional)")
    p.add_argument("--temp", dest="temperature", default=0.2, type=float)
    p.add_argument("--len", dest="length_scale", default=0.89, type=float)
    p.add_argument("--out", default="output.wav", help="Output WAV file")
    args = p.parse_args()
    sys.exit(synthesize(args.text, url=args.url, accent=args.accent, spk_name=args.spk_name,
                       temperature=args.temperature, length_scale=args.length_scale, out=args.out))