import requests
from .models import Movie
import os

def get_movie_data(request):

    imdb_key = os.environ.get('IMDB_API_KEY')

    url = 'https://api.themoviedb.org/3/movie/upcoming?language=en-US&append_to_response=images'
    query = {'api_key' : imdb_key }
    data = requests.get(url, params=query).json()

    movie_data = data['results']

    for movie in movie_data:
        name = movie['title']
        year = movie['release_date']
        plot = movie['overview']
        imdb_rating = movie['vote_average']
        poster = movie['poster_path']
        Movie(name=name, year=year, plot=plot, imdb_rating=imdb_rating, poster=poster).save()