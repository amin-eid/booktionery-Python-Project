from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),
    path('success',views.welcome),
    path('register',views.reg),
    path('register2',views.registration),
    path('login',views.login),
    path('logout',views.logout),
    path('<int:id>',views.user_profile),
]
