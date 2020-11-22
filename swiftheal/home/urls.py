from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("", views.index, name = 'home'),
    path("home", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("profile", views.profile, name = 'profile'),
    path("tips&facts", views.tips_facts, name = 'tips&facts')
]
