from django.shortcuts import render
from django.http import HttpResponse


# www.fulano.com.br/
# Host: 127.0.0.1:8000
# Path: /

def inicio(request):
    return render(request, 'inicio.html')
