<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_material, name='upload'),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_material, name='upload'),
>>>>>>> a5fbf081a135469b7d52e7f7e05a2c01f65b12b5
]