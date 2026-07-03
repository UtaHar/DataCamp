# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Exploratory analysis
print(netflix_df.describe())
print(netflix_df.info())
print(netflix_df['type'].unique())
print(netflix_df['genre'].unique())

# Subset movies from the nineties
nineties_movies = netflix_df[np.logical_and(netflix_df['release_year']>=1990, netflix_df['release_year']<2000,netflix_df['type']=='Movie')]
print(nineties_movies.describe())

# Extract the mode of the nineties movie duration
duration = nineties_movies['duration'].mode()[0]

print(f'The most common movie duration is', duration, 'minutes.')

# Plot the distribution of movie duration in the nineties.
plt.hist(nineties_movies['duration'])
plt.xlabel('Length of nineties movies')
plt.ylabel('Frequency')
plt.title('Many movies in the nineties were quite long.')
plt.show()

# Count movies shorter than 90 minutes
short_action_movies = nineties_movies[np.logical_and(nineties_movies['duration']<90, nineties_movies['genre']=='Action')]
print(short_action_movies.head())
short_movie_count = len(short_action_movies.index)

print(f'There are', short_movie_count, 'action movies shorter than 90 minutes in the nineties.')
