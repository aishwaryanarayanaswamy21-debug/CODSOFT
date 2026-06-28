# Task 5 -- Face Detection

This folder contains an OpenCV face detection demo for images, videos, and live webcam input.

## Features

- Detect faces in a still image
- Detect faces in a video file
- Detect faces from a webcam feed
- Label each detected face on screen
- Show the total face count in the current frame

## Files

- `face_detection.py` - main script
- `haarcascade_frontalface_default.xml` - local cascade file included in the folder
- `requirements.txt` - Python dependencies
- `src/images/` - sample images
- `src/videos/` - sample videos

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python face_detection.py
```

## Menu Options

1. Detect faces from an image
2. Detect faces from a video
3. Detect faces from a live webcam
4. Exit

## Notes

- The script uses the OpenCV Haar cascade face detector.
- The OpenCV package also provides its own built-in cascade data path.
- Press `q` to stop video or webcam detection.

