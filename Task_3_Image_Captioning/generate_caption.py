import sys
import os
import io
import csv
import requests
from pathlib import Path
from PIL import Image
import html as html_lib
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')
try:
    from transformers import BlipForConditionalGeneration, BlipProcessor
    import torch
except Exception as e:
    print("Missing required packages. Install from requirements.txt")
    raise

MODEL_NAME = "Salesforce/blip-image-captioning-base"

def load_image(path_or_url):
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        resp = requests.get(path_or_url)
        resp.raise_for_status()
        return Image.open(io.BytesIO(resp.content)).convert("RGB")
    else:
        return Image.open(path_or_url).convert("RGB")


def generate_caption(image, model, processor, device):
    if isinstance(image, str):
        image = load_image(image)
    inputs = processor(images=image, return_tensors="pt")
    
    for k, v in inputs.items():
        if hasattr(v, 'to'):
            inputs[k] = v.to(device)
    output_ids = model.generate(**inputs, max_length=64, num_beams=4)
    preds = processor.decode(output_ids[0], skip_special_tokens=True).strip()
    return preds


def main():
    # Accept either a single image path/URL or a directory containing images.
    target = None
    if len(sys.argv) < 2:
        try:
            target = input("Enter image path, image URL, or directory path (leave empty to exit): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nNo input provided. Exiting.")
            sys.exit(1)
        if not target:
            print("No input provided. Exiting.")
            sys.exit(1)
    else:
        target = sys.argv[1]

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Loading model {MODEL_NAME} on device {device}...")
    model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)
    processor = BlipProcessor.from_pretrained(MODEL_NAME)

    p = Path(target)
    # if target looks like a URL, treat as single image URL
    is_url = str(target).startswith("http://") or str(target).startswith("https://")

    image_paths = []
    if is_url:
        image_paths = [target]
    elif p.is_dir():
        exts = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".tiff"}
        for f in sorted(p.iterdir()):
            if f.is_file() and f.suffix.lower() in exts:
                image_paths.append(str(f))
        if not image_paths:
            print(f"No images found in directory: {p}")
            sys.exit(1)
    elif p.is_file():
        image_paths = [str(p)]
    else:
        print(f"Path not found: {target}")
        sys.exit(1)

    out_csv = Path(__file__).parent / "captions.csv"
    out_html = Path(__file__).parent / "report.html"
    print(f"Processing {len(image_paths)} image(s). Writing captions to: {out_csv} and {out_html}")

    results = []
    with out_csv.open("w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["image", "caption"])
        for img in image_paths:
            try:
                caption = generate_caption(img, model, processor, device)
                print(img, "->", caption)
                writer.writerow([img, caption])
                csvfile.flush()
                try:
                    os.fsync(csvfile.fileno())
                except Exception:
                    pass
                results.append((img, caption))
            except Exception as e:
                print(f"Failed for {img}: {e}")

    # Generate a simple, styled HTML report
    def _to_html_src(path_str, base_dir):
        # For URLs, return as-is. For local files, make relative path to base_dir.
        if str(path_str).startswith("http://") or str(path_str).startswith("https://"):
            return path_str
        try:
            p = Path(path_str).resolve()
            rel = os.path.relpath(p, base_dir)
            # Convert Windows backslashes to forward slashes for HTML
            return rel.replace('\\', '/')
        except Exception:
            return path_str

    html_parts = []
    html_parts.append("<!doctype html>")
    html_parts.append("<html><head><meta charset='utf-8'><title>Image Captioning Report</title>")
    html_parts.append("<style>body{font-family:Arial,Helvetica,sans-serif;margin:24px;background:#f7f9fb;color:#222}h1{margin-bottom:4px}header{margin-bottom:18px} .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px} .card{background:#fff;border-radius:8px;padding:10px;box-shadow:0 1px 4px rgba(16,24,40,0.08);overflow:hidden} .thumb{width:100%;height:180px;object-fit:cover;border-radius:6px;border:1px solid #eee} .meta{font-size:13px;color:#666;margin-top:8px} .caption{margin-top:6px;background:#f3f4f6;padding:8px;border-radius:6px;font-size:14px}</style>")
    html_parts.append("</head><body>")
    html_parts.append(f"<header><h1>Image Captioning Report</h1><div style='color:#444'>Model: {MODEL_NAME} • Generated: {datetime.utcnow().isoformat()} UTC</div></header>")
    html_parts.append("<section class='grid'>")

    base_dir = out_html.parent
    for img, caption in results:
        src = _to_html_src(img, base_dir)
        esc_caption = html_lib.escape(caption)
        filename = Path(img).name
        html_parts.append("<article class='card'>")
        html_parts.append(f"<img class='thumb' src=\"{src}\" alt=\"{html_lib.escape(filename)}\">")
        html_parts.append(f"<div class='meta'><strong>{html_lib.escape(filename)}</strong></div>")
        html_parts.append(f"<div class='caption'><span style='font-weight:700;color:#111;margin-right:8px;'>CAPTION:</span>{esc_caption}</div>")
        html_parts.append("</article>")

    html_parts.append("</section>")
    html_parts.append("</body></html>")

    try:
        out_html.write_text('\n'.join(html_parts), encoding='utf-8')
        print(f"Wrote HTML report: {out_html}")
    except Exception as e:
        print(f"Failed to write HTML report: {e}")

if __name__ == '__main__':
    main()
