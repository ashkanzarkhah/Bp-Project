from django.db import models
class Movie(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    movie_file = models.FileField(upload_to='movies/movie_files')

    def __str__(self):
        return self.title