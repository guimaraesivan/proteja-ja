from apps.usuarios.domain.entities import Usuario


class CriarUsuarioUseCase:
    def __init__(self, repository):
        self.repository = repository

    def executar(self, nome, email, senha):
        usuario = Usuario(nome, email, senha)

        if not usuario.is_valido():
            raise ValueError("Usuário inválido: verifique nome, e-mail e senha (mínimo 6 caracteres).")

        return self.repository.salvar(usuario)