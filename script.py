# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
# print(netflix_df)
# print(netflix_df[['release_year']])
filterd_movie_release = netflix_df[(netflix_df['release_year'] >= 1990) & (
    netflix_df['release_year'] <= 1999)]
# print(filterd_movie_release)
duration = 0
durations = filterd_movie_release['duration'].tolist()
duration = Counter(durations).most_common(1)[0][0]
print(duration)
print('test')
