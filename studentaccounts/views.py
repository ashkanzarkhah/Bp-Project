from django.shortcuts import render, redirect
from .forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View

class sign_upView(View):
    form_class = UserCreationForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'studentaccounts/signup.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('studentaccounts:main')
        return render(request, 'studentaccounts/signup.html', {'form': form})


class mainView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'studentaccounts/main.html')
        return redirect('studentaccounts:login')


class log_inView(View):
    form_class = AuthenticationForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'studentaccounts/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('studentaccounts:main')
        return render(request, 'studentaccounts/login.html', {'form': form})
