from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

# Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre
    
# Post
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='media')
    publicado = models.DateTimeField(default=timezone.now)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='posteos_usario')

    class Meta:
        ordering = ['publicado']

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()


class Comentario (models.Model):
    posts = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.texto

    def delete(self, using = None, keep_parents = False):
        super().delete()

    def save(self, *args, **kwargs):
        if self.pk:
            self.fecha_edicion = timezone.now()
        super().save(*args, **kwargs)

