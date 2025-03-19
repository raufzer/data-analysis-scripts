# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

filtered_movie_release = netflix_df[
    (netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999)
]
filtered_movie_release['duration'] = filtered_movie_release['duration'].str.extract(r'(\d+)')
filtered_movie_release['duration'] = pd.to_numeric(filtered_movie_release['duration'], errors='coerce')

durations = filtered_movie_release['duration'].dropna().tolist()
duration = Counter(durations).most_common(1)[0][0]
print(f'most frequent movie duration in the 1990s : {duration}')

plt.figure(figsize=(8, 5))
plt.title('Histogram of Movie Durations (1990s)')
plt.hist(durations, color='skyblue', alpha=0.7, edgecolor='black')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

filtered_movie_genre = filtered_movie_release[
    filtered_movie_release['listed_in'].str.contains('Action', na=False)
]
short_movie_count = sum(filtered_movie_genre['duration'] <= 90)
print(f'number of short action movies from the 1990s :{short_movie_count}')
