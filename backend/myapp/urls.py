from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('group', views.group_packages, name='group'),
    path('custom', views.custom_packages, name='custom'),
    path('flights', views.flights, name='flights'),
    path('flight/<str:pk>', views.flight, name='flight'),
    path('ticket', views.ticketing, name='ticketing'),
    path('cars', views.cars, name='cars'),
    path('gallery', views.gallery, name='gallery'),
    path('blogs', views.blog_list, name='blog_list'),
    path('blog/3', views.blog_detail, name='blog_detail'),    
    path('contacts', views.contacts, name='contacts'),

    path('main', views.main, name='main'),
    path('packages', views.packages, name='packages'),


]
