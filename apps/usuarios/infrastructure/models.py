from django.db import models


class UsuarioModel(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'usuarios'

    def __str__(self):
        return self.nome