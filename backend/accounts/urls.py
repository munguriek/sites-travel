from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='auth/login.html'), name='logout'),
    # path('register/', register, name='register'),

    # path('dashboard', views.dashboard, name='dashboard'),
    # path('profile/', views.profile, name='profile'),
    # path('logout/', views.logout, name='logout'),

    # path('activation/<str:pk>', views.activation, name='activation'),
    # path('approval/<str:pk>', views.approval, name='approval'),

    # path('users/', views.user_list, name='profile_list'),
  

]
