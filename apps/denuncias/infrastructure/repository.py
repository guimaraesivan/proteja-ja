from apps.denuncias.infrastructure.models import DenunciaModel
from apps.denuncias.domain.entities import Denuncia


class DenunciaRepository:
    def salvar(self, denuncia: Denuncia):
        denuncia_model = DenunciaModel.objects.create(
            nome_loja=denuncia.nome_loja,
            link_site=denuncia.link_site,
            motivo=denuncia.motivo
        )
        return denuncia_model

    def listar_todas(self):
        return DenunciaModel.objects.all()