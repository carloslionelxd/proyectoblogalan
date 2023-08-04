from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Usuario(AbstractUser):
    imagen = models.ImageField(null = True, blank = True, upload_to = 'usuarios', default = 'usuarios/user-default.png')
    telefono = models.CharField(max_length = 255)
    es_colaborador = models.BooleanField(default = False)
    es_miembro = models.BooleanField(default = True)

    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])

    def __str__(self):
        return self.username





