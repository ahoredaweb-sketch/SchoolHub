from django.urls import path
from . import views
from django.shortcuts import get_object_or_404, redirect
from .models import Material

def download(request, id):
    material = get_object_or_404(Material, id=id)
    material.downloads += 1
    material.save()
    return redirect(material.file.url)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_material, name='upload'),
    path('download/<int:id>/', views.download, name='download'),
]

def download(request, id):
    material = get_object_or_404(Material, id=id)
    material.downloads += 1
    material.save()
    return redirect(material.file.url)