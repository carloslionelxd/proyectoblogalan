from django.shortcuts import render
from django.http import HttpResponseNotFound

def index(request):
    return render(request, 'index.html')

def pagina_404 (request, exception):
    return HttpResponseNotFound('<h1> Página no encontrada </h1>')

def nosotrosView(request):
    return render(request, 'nosotros.html')