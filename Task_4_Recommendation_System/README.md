# Task 4 -- Movie Recommendation System

This folder contains a simple movie recommendation demo based on genre similarity.

## How It Works

- The script reads `movies.csv`
- It converts the `genre` column into feature vectors with `CountVectorizer`
- It computes cosine similarity between movies
- It recommends the most similar titles to the movie you enter

## Files

- `recommendation_system.py` - main script
- `movies.csv` - movie dataset used by the recommender
- `requirements.txt` - Python dependencies

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python recommendation_system.py
```

## Usage

1. Run the script.
2. Pick one of the movie titles printed on screen.
3. Enter the title exactly or close to it.
4. Review the top recommended movies and similarity scores.

## Notes

- The recommender is content-based, not collaborative.
- The dataset must stay in the same folder as the script.

