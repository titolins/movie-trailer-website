""" entertainment center module for the movie trailer website project.
this module is responsible for creating the list of movies to be passed to
fresh_tomatoes, which in turn generates the proper html page.
"""
import media
import fresh_tomatoes

# first movie attributes and instance
interstellar_poster_url = (
    "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5"
    "BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1__SX1381_SY722_.jpg"
    )
interstellar_trailer_url = "https://www.youtube.com/watch?v=0vxOhd4qlnA"
interstellar = media.Movie("Interstellar", interstellar_poster_url, 
                           interstellar_trailer_url)

# second movie attributes and instance
mad_max_poster_url = (
    "http://ia.media-imdb.com/images/M/MV5BMTUyMTE0ODcxNF5B"
    "Ml5BanBnXkFtZTgwODE4NDQzNTE@._V1__SX1381_SY722_.jpg"
    )
mad_max_trailer_url = "https://www.youtube.com/watch?v=hEJnMQG9ev8"
mad_max = media.Movie("Mad Max", mad_max_poster_url, mad_max_trailer_url)

# third movie attributes and instance
gotg_poster_url = (
    "http://ia.media-imdb.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJ"
    "eQWpwZ15BbWU4MDUxNDYxODEx._V1__SX1381_SY722_.jpg"
    )
gotg_trailer_url = "https://www.youtube.com/watch?v=d96cjJhvlMA"
gotg = media.Movie("Guardians of the Galaxy", gotg_poster_url, gotg_trailer_url)

# list of the movies instantiated
movies = [interstellar, mad_max, gotg]

# creating the html
fresh_tomatoes.open_movies_page(movies)
