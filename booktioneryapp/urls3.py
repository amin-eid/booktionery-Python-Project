from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.registration),
]
# <<<<<<< HEAD
#     path('user', views.user),
#     path('thanks', views.thanks),
#     path('admin2', views.admin2),
#     path('admin3', views.admin3),
#     path('admin4', views.admin4),
# =======
# <<<<<<< HEAD

# =======
# >>>>>>> 42bcbba83cd2e946a226e9217c0ce1ec0ee17637
# >>>>>>> 12b556b72a7873520cd0b60fc3ce4e8f8a1c6b0c
# ]