# Exploring Netflix Movies Dataset
- commits contain solving process step by step 
## Solution Explain
1. filitring netflix movies released between 90s by comparing subset dataframe of realse_year colmun with 90s 
2. finding the most frequent movie duration between 90s by converting my subset dataframe into a list then use a function counter to find the most repeated value
3. counting the movies with genre Action during 90s that their duration under 90 min

## Code Explain
1. creating a subset of the main dataframe by using new variable contains only rows with specific conditions (when you want to compare a column values you need to compare it with serie 'one-dimensional array' not dataframe 'two-dimensional labeled data structure')
2. converting my subset dataframe into with function .tolist() then use pre-defiend function counter from collections package
3. make another subset of my dataframe (the prevoius one with movies realesed in 90s) than iterating it with loops (you nned to use iterrows.() function and row,lab indexs) than compare each value of the current row with 90 min if condition is successed i add it to my count list
there is another method where i can directly make another the new subset of the dataframe with genre Action and realeased in 90s then then just count his len , will get the number of movies with genre Action in 90s with duration under 90 min
// code 
short_action_movies = action_movies[action_movies['duration'] < 90]
short_movie_count = len(short_action_movies)