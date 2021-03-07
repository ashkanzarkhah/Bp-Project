from django.shortcuts import render, redirect
from .forms import homeworkform
from .models import Homework

# Create your views here.
def homework_list(request):
    homeworks = Homework.objects.all().order_by('date')
    return render(request, 'homeworks/homework_list.html', {'homeworks' : homeworks})
def upload_homework(request):
    if request.method == 'POST':
        form = homeworkform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homeworks:list')
    form = homeworkform()
    return render(request, 'homeworks/homework_upload.html', {'form' : form})