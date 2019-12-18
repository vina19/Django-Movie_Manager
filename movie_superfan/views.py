from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Movie, Comment
from .forms import UserRegisterForm, CommentForm
from .views_movie_list import get_movie_data
from .views_movie_video import youtube_video
from django.utils import timezone

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
   
    query = request.GET.get('q')
    if query:
        queryset = movies.filter(name__icontains=query)

    return render(request, 'movie_superfan/movie_list.html', { 'movies' : movies , 'name' : 'List' })

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_video = youtube_video(movie)
    return render(request, 'movie_superfan/movie_detail.html', { 'movie' : movie })

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

@login_required
def user_profile(request):
    return render(request, 'movie_superfan/users/user_profile.html')

# @login_required
# def add_comment(request, movie_pk):

#     movie = get_object_or_404(Movie, pk=movie_pk)

#     if request.method == 'POST':

#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.movie = movie
#             comment.posted_date = timezone.now()
#             comment.save()
#             return redirect('movie_comment', comment_pk=comment.pk)
    
#     else:
#         form = CommentForm()
    
#     return render(request, 'movie_superfan/user_comment/add_comment.html', { 'form' : form, 'movie' : movie })

# def movie_comment(request, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     return render(request, 'movie_superfan/user_comment/movie_comment.html', { 'comment' : comment })