# Proteja-Já

Projeto Integrador (SENAC) — site colaborativo para denunciar lojas/sites
suspeitos de golpe, com cadastro/login de usuários e comentários nas denúncias.

## Stack

- Python 3.12+
- Django 6.1
- SQLite (banco padrão de desenvolvimento)
- Templates Django (HTML + CSS puro, sem framework de front-end)

## Arquitetura

O projeto segue uma organização em camadas (inspirada em Clean Architecture),
repetida em cada app (`usuarios`, `denuncias`, `comentarios`):

```
apps/<app>/
├── domain/          → entidades e regras de negócio puras (sem Django)
├── application/      → casos de uso (orquestram domain + repository)
├── infrastructure/   → models do Django e repositórios (acesso a dados)
├── interfaces/        → views (camada HTTP)
├── templates/<app>/  → HTML do app
├── urls.py
└── admin.py
```

## Apps

- **usuarios** — cadastro, login e logout. Usa o sistema de autenticação
  nativo do Django (`AbstractUser`), então as senhas são sempre
  criptografadas (hash), nunca salvas em texto puro. Login é feito por e-mail.
- **denuncias** — criar denúncia (exige login), listar denúncias, ver detalhe.
- **comentarios** — comentar em uma denúncia (exige login) e excluir o
  próprio comentário.

## Como rodar

```bash
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # opcional, para acessar /admin/

python manage.py runserver
```

Acesse http://127.0.0.1:8000/

## Rotas principais

| Rota | Descrição |
|---|---|
| `/` | Página inicial |
| `/usuarios/cadastro/` | Criar conta |
| `/usuarios/login/` | Entrar |
| `/usuarios/logout/` | Sair |
| `/denuncias/` | Lista de denúncias |
| `/denuncias/nova/` | Criar denúncia (login obrigatório) |
| `/denuncias/<id>/` | Detalhe da denúncia + comentários |
| `/admin/` | Painel administrativo do Django |

## Próximos passos sugeridos

- Upload de prints/evidências na denúncia (`ImageField`/`FileField`).
- Categorias de golpe (phishing, produto não entregue, clonagem de cartão etc.).
- Paginação na listagem de denúncias.
- API REST (Django REST Framework) caso um front-end separado (React/Vue) seja usado no futuro.
- Deploy (Render, Railway, PythonAnywhere) com `DEBUG=False`, `SECRET_KEY` via variável de ambiente e Postgres.
