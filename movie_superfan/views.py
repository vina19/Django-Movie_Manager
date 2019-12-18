from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import UserRegisterForm
from .views_movie_list import get_movie_data
from .views_movie_video import youtube_video

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    
    query = request.GET.get('q')
    if query:
        queryset = movies.filter(name__icontains=query)
    print(movies)
    return render(request, 'movie_superfan/movie_list.html', { 'movies' : movies, 'name' : 'List' })

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'movie_superfan/movie_detail.html', { 'movie' : movie })

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in!')
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'movie_superfan/users/user_register.html', { 'form' : form })

@login_required
def user_profile(request):
    return render(request, 'movie_superfan/users/user_profile.html')


# This is unlikely to be a useful view in your app but I wanted to get 
# the API call part working since i'm not seeing how you are invoking it. 
def test_movie_detail(request):
    # Pick a movie 
    get_movie_data(request)  # although I don't think you need to pass the request to this method 
    first_movie = Movie.objects.all()[0]  # whatever the first movie in the DB is
    youtube_video(first_movie)
    print(first_movie, first_movie.trailer)
    return render(request, 'movie_superfan/movie_detail.html', { 'movie': first_movie })


