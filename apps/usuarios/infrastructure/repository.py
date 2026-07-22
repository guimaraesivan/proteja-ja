from apps.usuarios.infrastructure.models import UsuarioModel
from apps.usuarios.domain.entities import Usuario


class UsuarioRepository:
    def salvar(self, usuario: Usuario):
        usuario_model = UsuarioModel.objects.create(
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha
        )
        return usuario_model

    def listar_todos(self):
        return UsuarioModel.objects.all()

    def buscar_por_email(self, email):
        return UsuarioModel.objects.filter(email=email).first()