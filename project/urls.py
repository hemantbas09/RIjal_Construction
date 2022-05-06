from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about_us/',views.about_us,name='aboutus'),
    path('awards/',views.awards,name='awards'),
    path('contact_us/',views.contact_us,name='contactus'),
    path('gallery/',views.gallery,name='gallery'),
    path('projects/',views.projects,name='project'),
    path('login/',views.login,name='login'),
]