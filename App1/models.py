from django.db import models

# Create your models here.
class Apps1(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def shortener(self):
        return self.body[:25] + '...'
