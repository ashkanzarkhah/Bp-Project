from django import forms
from .models import Movie

class movieform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'author', 'movie_file')