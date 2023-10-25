from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.zadanie, name = "zadanie"),
    path("answear/", views.answear, name = "answear"),
] 