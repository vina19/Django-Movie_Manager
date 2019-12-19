from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie, UserProfile
from .forms import UserRegisterForm, WatchedMovieForm
from .views_movie_list import get_movie_data
from .views_movie_video import youtube_video
from django.utils import timezone

# Create your views here.
# Display the movie list order by id
def movie_list(request):
    movies = Movie.objects.all().order_by('id')
   
    # Search bar which search the movie title
    query = request.GET.get('q')
    if query:
        movies = movies.filter(name__icontains=query)

    return render(request, 'movie_superfan/movie_list.html', { 'movies' : movies , 'title' : 'List' })

# Get the movie detail and the youtube video
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_video = youtube_video(movie)
    return render(request, 'movie_superfan/movie_detail.html', { 'movie' : movie })

# define marked watched and unwatched movie
def movie_watched(request,movie_pk):

    # if the movie watched then marked as false else true
    if request.user.is_authenticated:
        movie=get_object_or_404(Movie,pk=movie_pk)
        if movie.watched:
            movie.watched=False
        else:
            movie.watched=True
        movie.save()
        return render(request, 'movie_superfan/movie_detail.html', { 'movie' : movie })
    return redirect('user_login')


# Register form for the user
def user_register(request):
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in!')
            return redirect('user_login')
        else:
            messages.error(request, 'Please check the data you have entered')
            return render(request, 'movie_superfan/users/user_register.html', {'form' : form })
    
    else:
        form = UserRegisterForm()
        return render(request, 'movie_superfan/users/user_register.html', { 'form' : form })

# User profile with the watched movie
@login_required
def user_profile(request):
    watched = UserProfile.objects.all()
    return render(request, 'movie_superfan/users/user_profile.html', { 'watched' : watched })