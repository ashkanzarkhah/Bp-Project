from django.urls import include, path
from . import views
from .views import movie_listView, upload_movieView

app_name = 'movies'
urlpatterns = [
    path('list/', movie_listView.as_view(), name = 'list'),
    path('upload/', upload_movieView.as_view(), name = 'upload'),
]