from apps.denuncias.domain.entities import Denuncia


class CriarDenunciaUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, nome_loja, link_site, motivo):
        denuncia = Denuncia(nome_loja, link_site, motivo)

        if not denuncia.is_valida():
            raise ValueError("Denúncia inválida: nome da loja e motivo são obrigatórios.")

        return self.repository.salvar(denuncia)