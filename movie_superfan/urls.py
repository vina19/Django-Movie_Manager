from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, get_movie_list, get_movie_video

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('userprofile/', views.user_profile, name='user_profile'),
    path('registrationform/', views.user_register, name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name='movie_superfan/users/user_login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='movie_superfan/users/user_logout.html'), name='user_logout'),  
    #path('movievideo/', get_movie_video.get_youtube_link, name='movie_video'),
]