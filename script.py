# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

filterd_movie_release = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] <= 1999)]

durations = filterd_movie_release['duration'].tolist()
duration = Counter(durations).most_common(1)[0][0]
print(f'most frequent movie duration in the 1990s : {duration}')

plt.title('Histogram with the distributions of durations for movies released in the 1990s')
plt.hist(durations,color='skyblue', alpha=0.7, cumulative=False) 

filterd_movie_genre = filterd_movie_release[filterd_movie_release['genre'] == 'Action']
short_movie_count = 0
for lab, row in filterd_movie_genre.iterrows():
    if row['duration'] <= 90:
        short_movie_count += 1

print(f'number of short action movies from the 1990s :{short_movie_count}')
