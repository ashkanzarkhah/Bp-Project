from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def home(request):
    test = models.Apps1.objects.all().order_by('date')
    return render(request, 'App1/home.html',{'test': test})

def app_detail(request, slug):
    App = models.Apps1.objects.get(slug=slug)
    return render(request, 'App1/home.html', {'test': [App]})