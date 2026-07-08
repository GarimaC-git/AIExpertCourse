import time
import pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True)

# Load movie dataset
try:
    movies = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Movie dataset not found.")
    raise SystemExit

# Get all unique genres
genre_list = sorted(
    {
        genre.strip()
        for row in movies["Genre"].dropna().str.split(", ")
        for genre in row
    }
)

# Loading animation
def loading():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

# Convert polarity to sentiment
def sentiment_label(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"

# Display available genres
def choose_genre():
    print(Fore.GREEN + "\nAvailable Genres:")
    for index, genre in enumerate(genre_list, start=1):
        print(f"{index}. {genre}")

    while True:
        choice = input(Fore.YELLOW + "\nChoose a genre (number or name): ").strip()

        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(genre_list):
                return genre_list[number - 1]

        choice = choice.title()
        if choice in genre_list:
            return choice

        print(Fore.RED + "Invalid genre. Please try again.")

# Ask minimum rating
def choose_rating():
    while True:
        rating = input(
            Fore.YELLOW + "Minimum IMDb rating (7.6 - 9.3) or type 'skip': "
        ).strip()

        if rating.lower() == "skip":
            return None

        try:
            rating = float(rating)
            if 7.6 <= rating <= 9.3:
                return rating
        except ValueError:
            pass

        print(Fore.RED + "Please enter a valid rating.")

# Recommend movies
def movie_recommendation(genre=None, minimum_rating=None, positive_only=False, limit=5):

    filtered = movies

    if genre:
        filtered = filtered[
            filtered["Genre"].str.contains(genre, case=False, na=False)
        ]

    if minimum_rating is not None:
        filtered = filtered[
            filtered["IMDB_Rating"] >= minimum_rating
        ]

    if filtered.empty:
        return []

    filtered = filtered.sample(frac=1).reset_index(drop=True)

    recommendations = []

    for _, row in filtered.iterrows():

        overview = row["Overview"]

        if pd.isna(overview):
            continue

        polarity = TextBlob(overview).sentiment.polarity

        if positive_only and polarity < 0:
            continue

        recommendations.append(
            (
                row["Series_Title"],
                polarity
            )
        )

        if len(recommendations) == limit:
            break

    return recommendations

# Print movie recommendations
def display_movies(movie_list, username):

    print(Fore.CYAN + f"\nTop movie recommendations for {username}:\n")

    for i, (title, polarity) in enumerate(movie_list, start=1):
        print(
            Fore.GREEN +
            f"{i}. {title} | Sentiment: {sentiment_label(polarity)} ({polarity:.2f})"
        )

# ---------------- MAIN PROGRAM ---------------- #

print(Fore.BLUE + "===== AI Movie Recommendation System =====\n")

username = input(Fore.YELLOW + "Enter your name: ").strip()

if not username:
    username = "Guest"

print(Fore.GREEN + f"\nHello, {username}!")

selected_genre = choose_genre()

mood = input(
    Fore.YELLOW + "\nHow are you feeling today? "
).strip()

print(Fore.BLUE + "\nAnalyzing your mood", end="")
loading()

mood_score = TextBlob(mood).sentiment.polarity

print(
    Fore.GREEN +
    f"\nDetected Mood: {sentiment_label(mood_score)} ({mood_score:.2f})"
)

minimum_rating = choose_rating()

print(Fore.BLUE + "\nSearching for movies", end="")
loading()

movies_found = movie_recommendation(
    genre=selected_genre,
    minimum_rating=minimum_rating,
    positive_only=(mood_score >= 0),
    limit=5
)

if movies_found:
    display_movies(movies_found, username)
else:
    print(Fore.RED + "\nNo matching movies found.")

while True:

    again = input(
        Fore.YELLOW + "\nWould you like more recommendations? (yes/no): "
    ).strip().lower()

    if again == "yes":

        movies_found = movie_recommendation(
            genre=selected_genre,
            minimum_rating=minimum_rating,
            positive_only=(mood_score >= 0),
            limit=5
        )

        if movies_found:
            display_movies(movies_found, username)
        else:
            print(Fore.RED + "\nNo matching movies found.")

    elif again == "no":
        print(Fore.GREEN + f"\nEnjoy your movies, {username}! Goodbye!")
        break

    else:
        print(Fore.RED + "Please enter yes or no.")