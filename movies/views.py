from django.shortcuts import render, redirect
from .forms import movieform
from .models import Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies' : movies})
def upload_movie(request):
    if request.method == 'POST':
        form = movieform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:list')
    form = movieform()
    return render(request, 'movies/movie_upload.html', {'form' : form})