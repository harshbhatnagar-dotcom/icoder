from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
   path('', views.home,name="home"),  
   path('contact', views.contact,name="contact"),  
   path('about', views.about,name="about"),  
   path('search', views.search,name="search"),
   path("signup",views.signup,name="signup"),
   path("login",views.handlelogin,name="login"),
   path("logout",views.handlelogout,name="logout")
   
]