from .forms import RegistrarseForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .models import Usuario
from django.views.generic.detail import DetailView


class RegistroView(CreateView):
    template_name = 'registration/registro.html'
    form_class = RegistrarseForm

    

    def get_success_url(self):
        return reverse('usuarios:login')
    
class LoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('index')
    

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Sesión cerrada con exito.')

        return reverse('usuarios:login')

   
class UsuarioDetailView(DetailView):
        model = Usuario
        template_name = 'usuario/usuaeio_detail.html'
        context_object_name = 'posts'
        pk_url_kwarg = 'id'
        queryset = Usuario.objects.all()

  