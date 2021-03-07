from django.shortcuts import render, redirect
from .forms import homeworkform
from .models import Homework
from django.views import View

class movie_listView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            homeworks = Homework.objects.all().order_by('date')
            return render(request, 'homeworks/homework_list.html', {'homeworks': homeworks})
        return redirect('masteraccounts:login')

class upload_movieView(View):
    form_class = homeworkform
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.form_class()
            return render(request, 'homeworks/homework_upload.html', {'form': form})
        return redirect('masteraccounts:login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('homeworks:list')
            return render(request, 'homeworks/homework_upload.html', {'form': form})
        return redirect('masteraccounts:login')
