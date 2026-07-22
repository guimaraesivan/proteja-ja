class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def is_valido(self):
        return len(self.nome) > 0 and "@" in self.email and len(self.senha) >= 6
