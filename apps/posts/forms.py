#from django.forms import ModelForm
from django import forms
from .models import Post, Comentario

class CrearPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'texto', 'activo', 'categoria', 'imagen'] 
        labels = {
            'titulo': '',
            'subtitulo': '',
            'texto': '',
            'categoria': 'Categoría'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Ingrese el título', 'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'placeholder': 'Ingrese el resumen o copete', 'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'placeholder': 'Escriba la noticia', 'class': 'form-control', 'rows': 4}),
        }



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']




class EditarComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']