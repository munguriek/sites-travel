from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group', views.group_packages, name='group'),
    path('custom', views.custom_packages, name='custom'),
    path('ticket', views.ticketing, name='ticketing'),
    path('cars', views.cars, name='cars'),
    path('gallery', views.gallery, name='gallery'),
    path('blogs', views.blog_list, name='blog_list'),
    path('blog/<int>', views.blog_detail, name='blog_detail'),    
    path('contacts', views.contacts, name='contacts'),

    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    # path('profile/', views.profile, name='profile'),
    # path('activation/<str:pk>', views.activation, name='activation'),
    # path('approval/<str:pk>', views.approval, name='approval'),
    # path('users/', views.user_list, name='profile_list'),
  


]
