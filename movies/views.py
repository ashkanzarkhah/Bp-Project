from django.shortcuts import render, redirect
from .forms import movieform
from .models import Movie
from django.views import View

class movie_listView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            movies = Movie.objects.all().order_by('date')
            return render(request, 'movies/movie_list.html', {'movies': movies})
        return redirect('masteraccounts:login')

class upload_movieView(View):
    form_class = movieform
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.form_class()
            return render(request, 'movies/movie_upload.html', {'form': form})
        return redirect('masteraccounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('movies:list')
            return render(request, 'movies/movie_upload.html', {'form': form})
        return redirect('masteraccounts:login')

