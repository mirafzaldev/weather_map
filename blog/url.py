from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('weather/', views.weather,  name='blog-weather')
]

