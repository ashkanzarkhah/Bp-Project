from django import forms
from .models import Homework

class homeworkform(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ('title', 'homework_file')