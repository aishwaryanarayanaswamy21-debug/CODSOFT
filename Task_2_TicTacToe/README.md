# Task 2 -- Tic-Tac-Toe AI

This folder contains a console-based Tic-Tac-Toe game where the player competes against a minimax AI.

## How It Works

- The player uses `X`
- The computer uses `O`
- The AI evaluates available moves with minimax and chooses the best one
- The game ends when either side wins or the board is full

## Files

- `tic_tac_toe.py` - main game script
- `requirements.txt` - empty because the project uses only the Python standard library
- `demo_video_link.txt` - placeholder for a demo link
- `screenshots/` - sample gameplay screenshots

## Run

```bash
python tic_tac_toe.py
```

## Input Guide

Use board positions `1` through `9`:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

## Notes

- The AI is unbeatable when minimax is allowed to search the full game tree.
- If you enter an invalid move, the script asks again.

