import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_csv("movies.csv")

# Convert genres into numerical vectors
cv = CountVectorizer()
feature_matrix = cv.fit_transform(movies["genre"])

# Calculate similarity between movies
similarity = cosine_similarity(feature_matrix)


def recommend(movie_name):

    movie_name = movie_name.lower().strip()

    # Check whether movie exists
    if movie_name not in movies["title"].str.lower().values:
        print("\nMovie not found.")
        print("Please enter one of the following movies:\n")

        for movie in movies["title"]:
            print(movie)

        return

    # Find the movie index
    index = movies[movies["title"].str.lower() == movie_name].index[0]

    # Calculate similarity scores
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    selected_movie = movies.iloc[index]["title"]

    print("\nMovie Selected :", selected_movie)
    print("\nRecommended Movies:\n")

    rank = 1

    for movie_index, score in scores[1:6]:

        movie = movies.iloc[movie_index]

        print(f"{rank}. {movie['title']}")
        print(f"   Genre      : {movie['genre']}")
        print(f"   Similarity : {score * 100:.2f}%\n")

        rank += 1


print("Movie Recommendation System")
print()

print("Available Movies:\n")

for movie in movies["title"]:
    print(movie)

while True:

    movie = input("\nEnter Movie Name (or type 'exit'): ")

    if movie.lower() == "exit":
        print("\nThank you for using the Recommendation System.")
        break

    recommend(movie)