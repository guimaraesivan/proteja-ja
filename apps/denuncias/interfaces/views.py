from django.shortcuts import render, redirect
from apps.denuncias.application.use_cases import CriarDenunciaUseCase
from apps.denuncias.infrastructure.repository import DenunciaRepository


def criar_denuncia(request):
    if request.method == 'POST':
        nome_loja = request.POST.get('nome_loja')
        link_site = request.POST.get('link_site')
        motivo = request.POST.get('motivo')

        repository = DenunciaRepository()
        use_case = CriarDenunciaUseCase(repository)

        try:
            use_case.executar(nome_loja, link_site, motivo)
            return redirect('sucesso')
        except ValueError as erro:
            return render(request, 'denuncias/criar.html', {'erro': str(erro)})

    return render(request, 'denuncias/criar.html')