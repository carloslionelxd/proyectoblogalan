from django.urls import path
from . import views
from .views import LoginView, LogoutView, UsuarioDetailView
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registrarse/', views.RegistroView.as_view(), name='registrarse'), 
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('usuario-detail/<int:pk>/', UsuarioDetailView.as_view(), name = 'usuario-detail'),
]