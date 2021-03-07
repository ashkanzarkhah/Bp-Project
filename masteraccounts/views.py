from django.shortcuts import render, redirect
from .forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('masteraccounts:main')
    else: form = UserCreationForm()
    return render(request, 'masteraccounts/signup.html', {'form' : form})
def main(request):
    return render(request, 'masteraccounts/main.html')
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('masteraccounts:main')

    else:
        form = AuthenticationForm()
    return render(request, 'masteraccounts/login.html', {'form' : form})
