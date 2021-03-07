from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse


def home(request):
    return redirect('masteraccounts:signup')