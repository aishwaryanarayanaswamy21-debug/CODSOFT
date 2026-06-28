# CODSOFT AI Internship Projects

This repository contains the Python projects completed for the CodSoft Artificial Intelligence internship.

## Projects

| Task | Folder | Project | Main Tech |
|---|---|---|---|
| 1 | `Task_1_Chatbot` | Rule-based chatbot | Python standard library |
| 2 | `Task_2_TicTacToe` | Tic-Tac-Toe with AI | Python standard library |
| 3 | `Task_3_Image_Captioning` | Image captioning demo | Transformers, PyTorch, Pillow, Requests |
| 4 | `Task_4_Recommendation_System` | Movie recommendation system | Pandas, NumPy, scikit-learn |
| 5 | `Task_5_Face_Detection` | Face detection system | OpenCV |

## Repository Layout

```text
CODSOFT/
|-- README.md
|-- requirements.txt
|-- Task_1_Chatbot/
|-- Task_2_TicTacToe/
|-- Task_3_Image_Captioning/
|-- Task_4_Recommendation_System/
`-- Task_5_Face_Detection/
```

## Task Summary

### Task 1: Chatbot

A simple rule-based chatbot that responds to greetings, questions about time/date, and a few AI-related prompts.

### Task 2: Tic-Tac-Toe AI

A console-based Tic-Tac-Toe game where the player uses `X` and the computer uses `O` with a minimax strategy.

### Task 3: Image Captioning

A BLIP-powered image captioning script that accepts a local image, an image URL, or a directory of images and writes captions to CSV and HTML reports.

### Task 4: Recommendation System

A movie recommender that uses movie genres and cosine similarity to suggest similar titles.

### Task 5: Face Detection

An OpenCV-based face detection tool for images, videos, and live webcam input.

## Quick Start

Install the dependencies you need for a given task from that task's folder.

```bash
pip install -r Task_1_Chatbot/requirements.txt
pip install -r Task_2_TicTacToe/requirements.txt
pip install -r Task_3_Image_Captioning/requirements.txt
pip install -r Task_4_Recommendation_System/requirements.txt
pip install -r Task_5_Face_Detection/requirements.txt
```

Run each project from its folder:

```bash
python Task_1_Chatbot/chatbot.py
python Task_2_TicTacToe/tic_tac_toe.py
python Task_3_Image_Captioning/generate_caption.py path/to/image.jpg
python Task_4_Recommendation_System/recommendation_system.py
python Task_5_Face_Detection/face_detection.py
```

## Notes

- Task 3 downloads a pretrained model the first time it runs.
- Task 4 uses `movies.csv` in the same folder as the script.
- Task 5 uses the OpenCV Haar cascade classifier included with the OpenCV installation.

