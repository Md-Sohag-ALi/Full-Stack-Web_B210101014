from django.contrib import admin
from django.urls import path
from .views import home
#http://127.0.0.1:8000/first_app/home/
#http://127.0.0.1:8000/first_app/about/
urlpatterns = [
    path('home/',home ),
    
    # path('about/', ),
]
