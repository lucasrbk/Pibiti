import sys
from django.core.servers.basehttp import run
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import File
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from subprocess import run, PIPE
import requests
from django.core.files.storage import FileSystemStorage


def index(request):
    all_files = File.objects.all()
    template = 'files/index.html'
    context = {
        'all_files': all_files,
    }
    return render(request, template, context)


def detail(request):
    all_files = File.objects.all()
    return HttpResponse('html')


def button(request):
    return render(request, 'index.html')


def output_linear(request):
    if request.method == 'POST':
        import subprocess
        #output = subprocess.check_output(["C:\Users\Lucas\Desktop\Pibiti\algoritmos\linear.py", "--",
         #                                 request.POST['myFile']])
        #return HttpResponse(output, content_type='text/plain')


class FileAdd(CreateView):
    model = File
    fields = ['name', 'type', 'archive']
