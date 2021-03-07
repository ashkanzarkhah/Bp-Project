from django.urls import include, path
from . import views

app_name = 'homeworks'
urlpatterns = [
    path('list/', views.homework_list, name = 'list'),
    path('upload/', views.upload_homework, name = 'upload'),
]