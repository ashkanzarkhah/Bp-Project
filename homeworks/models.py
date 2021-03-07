from django.db import models
class Homework(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    homework_file = models.FileField(upload_to='homeworks/homework_files')

    def __str__(self):
        return self.title