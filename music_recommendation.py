
import pandas as pd

# Load the dataset
def load_songs(csv_file):
    try:
        songs = pd.read_csv(csv_file)
        return songs
    except FileNotFoundError:
        print("Dataset file not found!")
        return None

# Filter songs based on user preferences
def filter_songs(songs, genre=None, mood=None, artist=None, tempo_preference=None):
    filtered_songs = songs.copy()

    if genre:
        filtered_songs = filtered_songs[filtered_songs['Genre'].str.contains(genre, case=False, na=False)]

    if mood:
        filtered_songs = filtered_songs[filtered_songs['Mood'].str.contains(mood, case=False, na=False)]

    if artist:
        filtered_songs = filtered_songs[filtered_songs['Artist'].str.contains(artist, case=False, na=False)]

    if tempo_preference:
        if tempo_preference.lower() == 'fast':
            filtered_songs = filtered_songs[filtered_songs['Tempo'] >= 120]
        elif tempo_preference.lower() == 'slow':
            filtered_songs = filtered_songs[filtered_songs['Tempo'] < 120]

    return filtered_songs

# Main function
def main():
    songs = load_songs('songs_dataset.csv')  # CSV file name
    
    if songs is None:
        return

    print("Welcome to the Music Recommendation System!")
    
    # Take user inputs
    genre = input("Enter preferred genre (or press Enter to skip): ")
    mood = input("Enter your current mood (or press Enter to skip): ")
    artist = input("Enter favorite artist (or press Enter to skip): ")
    tempo_preference = input("Do you prefer fast or slow songs? (fast/slow/press Enter to skip): ")

    # Filter songs
    recommendations = filter_songs(songs, genre, mood, artist, tempo_preference)

    # Display recommendations
    if not recommendations.empty:
        print("\nRecommended Songs:")
        print(recommendations[['Song Title', 'Artist', 'Genre', 'Mood', 'Tempo']].head(10))  # Display top 10
    else:
        print("\nNo songs found matching your preferences.")

if __name__ == "__main__":
    main()
    