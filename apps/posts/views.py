from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comentario, Categoria
from .forms import CrearPostForm, ComentarioForm, EditarComentarioForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.usuarios.mixins import EsColaboradorMixin


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_seleccionada = self.request.GET.get('categoria')
        if categoria_seleccionada:
            queryset = queryset.filter(categoria = categoria_seleccionada)
        orden = self.request.GET.get('orderby')
        if orden:
            if orden == 'fecha_asc':
                queryset = queryset.order_by('fecha')
            elif orden == 'fecha_desc':
                queryset = queryset.order_by('-fecha')
            elif orden == 'alf_asc':
                queryset = queryset.order_by('titulo')
            elif orden == 'alf_desc':
                queryset = queryset.order_by('-titulo')

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all
        return context

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm() 
        context['comentarios'] = Comentario.objects.filter(posts_id=self.kwargs['id'])
        return context

    def post(self, request, *args, **kwargs):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.posts_id = self.kwargs['id']
            comentario.save()
            return redirect('apps.posts:post_individual', id=self.kwargs['id'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class Postear(LoginRequiredMixin, EsColaboradorMixin, CreateView):
    model = Post
    template_name = 'posts/postear.html'
    form_class = CrearPostForm

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('apps.posts:posts')
    
# Vista para actualizar una publicacion ya existente
class EditarPost(LoginRequiredMixin, EsColaboradorMixin, UpdateView):
    model = Post
    template_name = 'posts/editar-post.html'
    form_class = CrearPostForm # Uso el mismo de crear una publicacion

    def get_success_url(self):
        return reverse('apps.posts:posts')
    
# Vista que elimina un posteo
class EliminarPost(LoginRequiredMixin, EsColaboradorMixin, DeleteView):
    template_name = 'posts/eliminar-post.html' # Es un template intermedio -esta seguro s-n-
    model = Post


    def get_success_url(self):
        return reverse('apps.posts:posts')
    
class EliminarComentario(LoginRequiredMixin, EsColaboradorMixin, DeleteView):
    template_name = 'posts/eliminar-comentario.html'
    model = Comentario

    def get_success_url(self):
            return reverse('apps.posts:post_individual', args = [self.object.posts.id]) 
    


class EditarComentario(LoginRequiredMixin, EsColaboradorMixin, UpdateView):
    model = Comentario
    template_name = 'posts/editar-comentario.html'
    form_class = EditarComentarioForm
    success_url = reverse_lazy('apps.posts:posts')

    def get_success_url(self):
        return reverse('apps.posts:post_individual', kwargs={'id': self.object.posts.id})
    
