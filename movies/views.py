from django.shortcuts import render, redirect
from .forms import movieform
from .models import Movie

# Create your views here.
def movie_list(request):
    if request.user.is_authenticated:
        movies = Movie.objects.all().order_by('date')
        return render(request, 'movies/movie_list.html', {'movies' : movies})
    return redirect('masteraccounts:login')
def upload_movie(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = movieform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('movies:list')
        form = movieform()
        return render(request, 'movies/movie_upload.html', {'form' : form})
    return redirect('masteraccounts:login')