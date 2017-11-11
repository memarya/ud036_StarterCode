import os
import media
import fresh_tomatoes

"""Creates instances of the movie class using
   externally stored movies data and creates
   a list from these instances.

"""

movie_data_file = os.getcwd() + '\movies.txt'
movies = []
with open(movie_data_file, 'rt') as f:
    for line in f:
        title, img, trailerURL = line.split(',')
        movie = media.Movie(title, img, trailerURL)
        movies.append(movie)

fresh_tomatoes.open_movies_page(movies)
