from django.urls import path
from . import views, get_movie_list

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('userprofile/', views.user_profile, name='user_profile')
]