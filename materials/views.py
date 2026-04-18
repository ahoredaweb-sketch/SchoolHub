<<<<<<< HEAD
from django.shortcuts import render, redirect
from .models import Material

def home(request):
    materials = Material.objects.all().order_by('-id')
    return render(request, 'materials/home.html', {'materials': materials})


def upload_material(request):
    if request.method == 'POST':
        Material.objects.create(
            title=request.POST['title'],
            course=request.POST['course'],
            file=request.FILES['file'],
            uploaded_by=None
        )
        return redirect('home')

=======
from django.shortcuts import render, redirect
from .models import Material

def home(request):
    materials = Material.objects.all().order_by('-id')
    return render(request, 'materials/home.html', {'materials': materials})


def upload_material(request):
    if request.method == 'POST':
        Material.objects.create(
            title=request.POST['title'],
            course=request.POST['course'],
            file=request.FILES['file'],
            uploaded_by=None
        )
        return redirect('home')

>>>>>>> a5fbf081a135469b7d52e7f7e05a2c01f65b12b5
    return render(request, 'materials/upload.html')