# Exploring Netflix Movies Dataset
- commits contain solving process step by step 
## Solution Explain
1. filitring netflix movies released between 90s & 99s by comparing subset dataframe of realse_year colmun with 90s & 99s
2. finding the most frequent movie duration between 90s & 99s by converting my subset dataframe into a list then use a function counter to find the most repeated value

## Code Explain
1. creating a subset of the main dataframe by using new variable contains only rows with specific conditions (when you want to compare a column values you need to compare it with serie 'one-dimensional array' not dataframe 'two-dimensional labeled data structure')
2. converting my subset dataframe into with function .tolist() then use pre-defiend function counter from collections package