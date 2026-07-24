from django.urls import path
from apps.denuncias.interfaces.views import criar_denuncia

urlpatterns = [
    path('nova/', criar_denuncia, name='criar_denuncia'),
]