import requests
from .models import Movie

def get_movie_data(request):

    url = 'https://api.themoviedb.org/3/movie/upcoming?language=en-US&api_key=e57a66af857105a473e4b8fb6d45c63e&append_to_response=videos,images'
    data = requests.get(url).json()

    movie_data = data['results']

    for movie in movie_data:
        name = movie['title']
        year = movie['release_date']
        plot = movie['overview']
        imdb_rating = movie['vote_average']
        poster = movie['poster_path']
        Movie(name=name, year=year, plot=plot, imdb_rating=imdb_rating, poster=poster).save()