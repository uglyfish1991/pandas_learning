import pandas as pd

# The dataset might shorten itself to fit nicely on the screen.
# If you want to see all rows without any truncation, we can turn off this default behaviour with the following:
pd.set_option('display.max_rows', None)

# Reading the CSV file into a DataFrame (a table-like structure) and giving it the name "df"
df = pd.read_csv("spotify_songs.csv")

# The 'df.shape' gives us the number of rows and columns in the DataFrame.
# The 'df.columns' lists the names of all the columns.
# These are useful to understand the structure of our dataset at a glance.
print(df.shape)
print(df.columns)

# 'df.head()' shows us the first few rows of the DataFrame.
# This is a good way to quickly inspect the first five records and get an idea of what the data looks like.
print(df.head())

# Counting the unique values in the "playlist_genre" column to see how many songs belong to each genre.
print(df["playlist_genre"].value_counts())

# Finding the most common genre using the mode (the value that appears the most often).
print(df["playlist_genre"].mode()[0])

# Calculating the median (middle value) of the "duration_ms" column, which holds the song durations in milliseconds.
print(df["duration_ms"].median())

# Calculating the mean (average) of the song durations in milliseconds.
print(df["duration_ms"].mean())

# Finding the longest song's duration (max) and the shortest song's duration (min).
# Then printing the difference between the longest and shortest song, which tells us the range of song lengths.
max_duration = df["duration_ms"].max()
min_duration = df["duration_ms"].min()
print(max_duration - min_duration)

# Summing up all the song durations in the dataset, to get the total duration of all songs combined.
print(df["duration_ms"].sum())

# Sorting the DataFrame by song duration, from longest to shortest (descending order).
print(df.sort_values(by=["duration_ms"], ascending=False))

# Sorting the DataFrame alphabetically by the "track_name" column.
print(df.sort_values(by=["track_name"]))

# Grouping the songs by genre and finding the shortest song duration in each genre.
print(df.groupby("playlist_genre")["duration_ms"].min())

# Using a query to find all songs by Ricky Martin in the dataset.
print(df.query("track_artist=='Ricky Martin'"))

# Calculating the mean duration again and storing it in a variable called 'mean_value'.
mean_value = df["duration_ms"].mean()

# Using a query to find all songs that are longer than the average (mean) duration.
print(df.query("duration_ms > @mean_value"))
