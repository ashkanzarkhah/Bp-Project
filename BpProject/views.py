from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views import View
class homeView(View):
    def get(self, request, *args, **kwargs):
        return redirect('masteraccounts:login')
