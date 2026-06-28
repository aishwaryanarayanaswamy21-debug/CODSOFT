# Task 3 -- Image Captioning

This folder contains a BLIP-based image captioning script.

## Features

- Accepts a local image path
- Accepts an image URL
- Accepts a directory of images
- Generates captions using a pretrained `Salesforce/blip-image-captioning-base` model
- Writes results to both `captions.csv` and `report.html`

## Files

- `generate_caption.py` - main captioning script
- `captions.csv` - generated output file
- `report.html` - generated HTML report
- `images/` - sample images
- `requirements.txt` - Python dependencies

## Install

```bash
pip install -r requirements.txt
```

## Run

Caption a single image:

```bash
python generate_caption.py path/to/image.jpg
```

Caption an image from a URL:

```bash
python generate_caption.py https://example.com/image.jpg
```

Caption every image in a folder:

```bash
python generate_caption.py path/to/image-folder
```

## Notes

- The first run downloads the pretrained model weights.
- If CUDA is available, the script will use the GPU automatically.
- Internet access is required for URL input and for the initial model download.

