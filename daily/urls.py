from django.urls import path
from . import views
app_name = 'daily'

urlpatterns = [
    path('', views.index, name='index'),
    path('/login', views.login, name='login'),
    path('/join', views.join, name='join'),
]
