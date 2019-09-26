from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import File
from django.shortcuts import render


def index(request):
    all_files = File.objects.all()
    context = {
        'all_files': all_files,
    }
    return render(request, 'files/index.html', context)


def detail(request):
    all_files = File.objects.all()

    return HttpResponse('html')
