class Denuncia:
    def __init__(self, nome_loja, link_site, motivo):
        self.nome_loja = nome_loja
        self.link_site = link_site
        self.motivo = motivo

    def is_valida(self):
        return len(self.nome_loja) > 0 and len(self.motivo) > 0
    