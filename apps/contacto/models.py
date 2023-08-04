from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length = 100)
    email = models.EmailField()
    asunto = models.CharField(max_length = 50, default = "sin asunto")
    mensaje = models.CharField(max_length = 255)
    numero_tel = models.CharField(max_length = 20)

    def __str__(self):
        return self.asunto

