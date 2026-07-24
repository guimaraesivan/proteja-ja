from django.urls import path
from apps.usuarios.interfaces.views import cadastrar_usuario

urlpatterns = [
    path('cadastro/', cadastrar_usuario, name='cadastrar_usuario'),
]