from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_superfan/home_page.html', { 'movies' : movies })

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'movie_superfan/movie_detail_page.html', { 'movie' : movie })

def user_profile(request):
    return render(request, 'movie_superfan/userprofile_page.html')