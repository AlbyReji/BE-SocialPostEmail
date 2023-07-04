from django.urls import path 
from .import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('',views.login , name = 'login'),
    path('home',views.home , name = 'home'),
    path('base/',views.base , name = 'base'),
    path('register/',views.register , name = 'register'),
    path('addpost/',views.addpost , name = 'addpost'),
    path('logout/',auth.LogoutView.as_view(template_name = 'postapp_temp/login.html'),name="logout"),
    path('edit/<uuid:postid>/', views.editpost, name='editpost'),
    path('delete/<uuid:postid>/', views.delete, name='delete'),


]