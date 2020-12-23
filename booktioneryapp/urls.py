from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),
    path('success',views.welcome),
    path('register',views.registration),
    path('login',views.login),
    path('logout',views.logout),
]
