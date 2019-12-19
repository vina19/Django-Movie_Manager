from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Movie
from .forms import UserRegisterForm
from .views_movie_list import get_movie_data
from .views_movie_video import youtube_video
from django.utils import timezone

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all().order_by('id')
   
    query = request.GET.get('q')
    if query:
        movies = movies.filter(name__icontains=query)

    return render(request, 'movie_superfan/movie_list.html', { 'movies' : movies , 'title' : 'List' })

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_video = youtube_video(movie)
    return render(request, 'movie_superfan/movie_detail.html', { 'movie' : movie })

def search_movie(request):
    if request.method == 'POST':
        if not request.POST['search']:
            return redirect('logged_in')
        # Get all matches movie from the search input from the user    
        if '-w' in request.POST['search']:
            Q=re.findall('(.*)\s+-w',request.POST['search'])

            # if not match, filter by the unwatched movie else
            # get the name, year, and genre of the movie. 
            if not Q:
                movies=Movie.objects.filter(Watched=False)
                return render(request,'main.html',{'movies':movies})
            else:
                Q=Q[0]
                list1=Movie.objects.filter(Name__contains=Q,Watched=False)
                list2=Movie.objects.filter(Year__contains=Q,Watched=False)
                list3=Movie.objects.filter(Genre__contains=Q,Watched=False)

        # if movie found get the name, year, and genre.
        else:
            Q=request.POST['search']
            list1=Movie.objects.filter(Name__contains=Q)
            list2=Movie.objects.filter(Year__contains=Q)
            list3=Movie.objects.filter(Genre__contains=Q)

        # Set context with the list objects.
        res=list(set(list1)^set(list2)^set(list3))
        context={
            'movies':res,
        }
    return render(request, 'movie_list.html', context)

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

# define favorite movies
@login_required
def Favorite(request, movie_pk):

    # if it's the favorite movie to watch then false else true
    movie=get_object_or_404(Movie, pk=movie_pk)
    if movie.Watched:
        movie.Watched=False
    else:
        movie.Watched=True
    movie.save()
    return redirect('user_login')

# define marked watched and unwatched movie
@login_required
def Watched(request, movie_pk):

    # if the movie watched then marked as false else true
    movie=get_object_or_404(Movie, pk=movie_pk)
    if movie.Watched:
        movie.Watched=False
    else:
        movie.Watched=True
    movie.save()
    return render(request,'movie_detail.html', { 'movie': movie })
    