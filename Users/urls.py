from django.urls import include, path
from . import views

app_name = 'Users'
urlpatterns = [
    path('signup', views.signup_view, name='signup'),
]