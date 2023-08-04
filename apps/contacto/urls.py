from django.urls import path
from . import views

urlpatterns = [
    path('contacto/', views.contactoView, name = 'contacto'),
]