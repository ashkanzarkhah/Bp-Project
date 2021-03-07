from django.urls import include, path
from . import views

app_name = 'studentaccounts'
urlpatterns = [
    path('signup/', views.sign_up, name = 'signup'),
    path('main/', views.main, name = 'main'),
    path('login/', views.log_in, name = 'login'),
]