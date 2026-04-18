from django.shortcuts import render, redirect
from .models import Material

def home(request):
    materials = Material.objects.all().order_by('-id')
    return render(request, 'materials/home.html', {'materials': materials})


def upload_material(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return render(request, 'materials/upload.html', {
                'error': 'No file selected'
            })

        Material.objects.create(
            title=request.POST.get('title'),
            course=request.POST.get('course'),
            file=request.FILES['file'],
            uploaded_by=None
        )

        return redirect('home')

    return render(request, 'materials/upload.html')