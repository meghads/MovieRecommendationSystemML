# -*- coding: utf-8 -*-
"""Movie recommendation system ML.ipynb

**Content based and popular based recommendation system**

**Importing the dependencies**
"""

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""**Data collection and preprocessing**"""

# Loading the data from the csv file to a pandas dataframe
movies_data = pd.read_csv('/content/movies.csv')

# Print first 5 rows of dataframe
movies_data.head()

# Number of rows and columns in dataframe
movies_data.shape

# Selecting the relevent features for recommendation
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
print(selected_features)

# Replacing the missing values with null string
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')

# Combining all the 5 selected features
combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

print(combined_features)

# Converting the text data to feature vectors
vectorizer = TfidfVectorizer()

featured_vectors = vectorizer.fit_transform(combined_features)

print(featured_vectors)

"""**Cosine similarity**"""

# Getting the similarity scores using codine similarity
similarity = cosine_similarity(featured_vectors)
print(similarity)

similarity.shape

# Getting the movie name from the user
movie_name = input('Enter your favourite movie name: ')

# Creating a list with all the movie names given in the dataset
list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)

# Finding the close match for the movie name given by the user
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

# Finding the index of the movie with title
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

# Getting the list of similar movies
similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

len(similarity_score)

# Sorting the movies based on the similarity score
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)

# Print the name of similar movies based on the index
print('Movies suggested for you: \n')
i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index == index]['title'].values[0]
  if (i<16):
    print(i, '.', title_from_index)
    i+=1

"""**Movie recommendation system**"""

movie_name = input('Enter your favourite movie name : ')
list_of_all_titles = movies_data['title'].tolist()
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
similarity_score = list(enumerate(similarity[index_of_the_movie]))
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print('Movies suggested for you : \n')
i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<16):
    print(i, '.',title_from_index)
    i+=1
