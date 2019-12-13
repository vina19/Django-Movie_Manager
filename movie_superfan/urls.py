from django.urls import path
from . import views, get_movie_list, get_movie_video

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('userprofile/', views.user_profile, name='user_profile'),
    path('registrationform/', views.user_register, name='user_register'),    
    #path('movievideo/', get_movie_video.get_youtube_link, name='movie_video'),
]