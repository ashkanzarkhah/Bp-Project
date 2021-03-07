from django.urls import include, path
from . import views
from .views import sign_upView, mainView, log_inView

app_name = 'studentaccounts'
urlpatterns = [
    path('signup/', sign_upView.as_view(), name = 'signup'),
    path('main/', mainView.as_view(), name = 'main'),
    path('login/', log_inView.as_view(), name = 'login'),
]