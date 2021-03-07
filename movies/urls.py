from django.urls import include, path
from . import views

app_name = 'movies'
urlpatterns = [
    path('list/', views.movie_list, name = 'list'),
    path('upload/', views.upload_movie, name = 'upload'),
]