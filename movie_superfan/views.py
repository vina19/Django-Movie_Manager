from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_superfan/homepage.html', { 'movies' : movies })

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, 'movie_superfan/movie_detail_page.html', { 'movie' : movie })

def user_profile(request):
    return render(request, 'movie_superfan/userprofile_page.html')

def get_youtube_link(movie):
    # https://docs.python.org/3/library/urllib.parse.html
    # I use the quote_plus to replaces the spaces with the plus sign, so I can
    # add the query to the youtube url with the name of the movie from the movie that we have.
    query = urllib.quote_plus(movie.name)

    response = urllib.urlopen('https://www.youtube.com/results?search_query='+query+'+trailer').read()

    soup = BeautifulSoup(response, "lmxl")

    movie_trailers = soup.find_all('ol', {'class':'yt-uix-sessionlink'})[0]

    for trailer in movie_trailers:
        item = trailer[0].find_all('a',{'class':'yt-uix-sessionlink'})[0]
    item = re.findall('=(.*)',item.get('href'))
    print(item)

    link = 'http://www.youtube.com/embed/'+item[0]
    movie.trailer=link
    movie.save()