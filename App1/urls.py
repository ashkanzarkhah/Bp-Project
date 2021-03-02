from django.urls import include, path
from . import views

app_name = "App1"
urlpatterns = [
    path('', views.home, name="write"),
    path('<slug>', views.app_detail, name="detail"),
]