# Controle de Estoque - API REST

API desenvolvida com Django e Django REST Framework pra gerenciar estoque de produtos.

## Sobre o Projeto

Esse projeto tá sendo desenvolvido pra facilitar o controle de estoque de uma empresa. Por enquanto é a estrutura básica mas a ideia é implementar um CRUD completo de produtos com todas as funcionalidades necessárias.

## Tecnologias

- Python 3.x
- Django 4.2.7
- Django REST Framework 3.14.0
- SQLite (banco de dados)

## Como Rodar o Projeto

Primeiro, clone o repositório:

```bash
git clone https://github.com/van-dik/controle-estoque.git
cd controle-estoque
```

Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Rode as migrações do banco de dados:

```bash
python manage.py migrate
```

Crie um superusuário pra acessar o admin:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse http://localhost:8000/admin/ pra entrar no painel administrativo.

