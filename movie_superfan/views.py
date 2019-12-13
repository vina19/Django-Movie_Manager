from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie
from .forms import UserRegisterForm

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()

    query = request.GET.get('q')
    if query:
        queryset = movies.filter(name__icontains=query)

    return render(request, 'movie_superfan/homepage.html', { 'movies' : movies }, { 'name' : 'List'})

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'movie_superfan/movie_detail_page.html', { 'movie' : movie })

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('movie_list')
    else:
        form = UserRegisterForm()
    return render(request, 'movie_superfan/user_register.html', { 'form' : form })

def user_profile(request):
    return render(request, 'movie_superfan/userprofile_page.html')