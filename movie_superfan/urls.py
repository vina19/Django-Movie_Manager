from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#app_name = 'movie_superfan'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    # path('<int:movie_pk>/comment/add/', views.add_comment, name='add_comment'),
    # path('comment/detail/<int:comment_pk>/', views.movie_comment, name='movie_comment'),
    path('userprofile/', views.user_profile, name='user_profile'),
    path('registrationform/', views.user_register, name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name='movie_superfan/users/user_login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='movie_superfan/users/user_logout.html'), name='user_logout'),
]