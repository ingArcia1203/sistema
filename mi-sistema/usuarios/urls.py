from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_usuario, name='registrar_usuario'),
    path('consultar/', views.lista_usuarios, name='lista_usuarios'),
]