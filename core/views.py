from django.shortcuts import render
from .models import Post1
# Create your views here.


def bir(request):
    malumotlar = Post1.objects.all()
    qolip = {
        'malumotlar': malumotlar
    }
    return render(request, 'index.html', qolip)

    
