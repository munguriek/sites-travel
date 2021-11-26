from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('group', views.group_packages, name='group'),
    path('custom', views.custom_packages, name='custom'),
    path('flight_list', views.flight_list, name='flight_list'),
    path('ticket', views.ticketing, name='ticketing'),
    path('car_list', views.car_list, name='car_list'),
    path('gallery', views.gallery, name='gallery'),
    path('blogs', views.blog_list, name='blog_list'),
    path('blog/3', views.blog_detail, name='blog_detail'),    
    path('contacts', views.contacts, name='contacts'),

    path('main', views.main, name='main'),
    path('packages', views.packages, name='packages'),
    path('flights', views.flights, name='flights'),
    path('cars', views.cars, name='cars'),



]
