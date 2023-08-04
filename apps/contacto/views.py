from django.shortcuts import render
from .models import Contacto  

# Create your views here.
def contactoView (request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        numero_tel = request.POST.get('numero_tel')
        contacto = Contacto(nombre=nombre, email=email,asunto=asunto, mensaje=mensaje, numero_tel=numero_tel)
        contacto.save()

    return render(request, 'contacto.html', {})

