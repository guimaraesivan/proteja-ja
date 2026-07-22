from django.shortcuts import render, redirect
from apps.usuarios.application.use_cases import CriarUsuarioUseCase
from apps.usuarios.infrastructure.repository import UsuarioRepository


def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        repository = UsuarioRepository()
        use_case = CriarUsuarioUseCase(repository)

        try:
            use_case.executar(nome, email, senha)
            return redirect('sucesso')
        except ValueError as erro:
            return render(request, 'usuarios/cadastro.html', {'erro': str(erro)})

    return render(request, 'usuarios/cadastro.html')