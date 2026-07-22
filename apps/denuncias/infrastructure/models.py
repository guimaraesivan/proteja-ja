from django.db import models


class DenunciaModel(models.Model):
    nome_loja = models.CharField(max_length=255)
    link_site = models.URLField(max_length=500)
    motivo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'denuncias'

    def __str__(self):
        return self.nome_loja