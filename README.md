# Project Title: Exploring Netflix Movies of the 1990s

## Project Objective:
- To analyze Netflix movies released in the 1990s.
- To identify trends in movie duration and genre popularity.

## Data Source:
- Netflix Movies Dataset (Link)

## Methodology:

### Data Filtering:
- Filtered the dataset to include only movies released between 1990 and 1999.

### Frequent Movie Duration:
- Identified the most common movie duration using Python's Counter function.

### Short Action Movies:
- Counted the number of action movies with a duration of less than 90 minutes.

## Code Explain:
Check scripts.py file.
1. Creating a subset of the main dataframe by using new variable contains only rows with specific conditions (when you want to compare a column values you need to compare it with serie 'one-dimensional array' not dataframe 'two-dimensional labeled data structure')
2. Converting my subset dataframe into a list with function .tolist() (1D array serie to list) then use pre-defiend function counter from collections package
3. Make another subset of my dataframe (the prevoius one with movies realesed in 90s) which is movies with genre Action than iterating it with loops (you need to use iterrows.() function and row,lab indexs) than compare each value of the current row with 90 min if condition is successed i add it to my count list
here is another method:
make a subset again from the one with genre Action but with condition then just count their len which is count 'number' of movies etc ..
// Code 
short_action_movies = action_movies[action_movies['duration'] < 90]
short_movie_count = len(short_action_movies)

## Results:
Most Frequent Duration: [Insert the most frequent duration here]
Number of Short Action Movies: [Insert the count here]
## Visualizations:
Soon

## Conclusions:
Soon

## Future Work:
Soon