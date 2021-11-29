from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('group', views.group_trips, name='group_trips'),
    path('group/<int:pk>', views.group_trip, name='group_trip'),

    path('custom', views.custom_trips, name='custom'),

    path('flight_list', views.flight_list, name='flight_list'),
    path('flight_detail/<str:pk>', views.flight_detail, name='flight_detail'),

    path('car_list', views.car_list, name='car_list'),
    path('car_detail/<str:pk>', views.car_detail, name='car_detail'),

    path('gallery', views.gallery, name='gallery'),
    path('blogs', views.blog_list, name='blog_list'),
    path('blog/3', views.blog_detail, name='blog_detail'),    
    path('contacts', views.contacts, name='contacts'),

    path('main', views.main, name='main'),
    path('packages', views.packages, name='packages'),
    path('flights', views.flights, name='flights'),
    path('cars', views.cars, name='cars'),
    path('bookings', views.bookings, name='bookings'),

]
