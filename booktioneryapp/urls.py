from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.register),
    path('user', views.user),
    path('thanks', views.thanks),
    path('admin2', views.admin2),
    path('admin3', views.admin3),
    path('admin4', views.admin4),
]