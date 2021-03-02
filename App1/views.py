from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    test = models.Apps1.objects.all().order_by('date')
    return render(request, 'App1/home.html',{'test': test})
