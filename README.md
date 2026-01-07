# Controle de Estoque - API REST

API desenvolvida com Django e Django REST Framework pra gerenciar estoque de produtos.

## Sobre o Projeto

Esse projeto é uma API REST que permite cadastrar produtos, consultar, atualizar e deletar. Também dá pra adicionar e remover itens do estoque e ver quais produtos tão com estoque baixo.

## Funcionalidades

- CRUD completo de produtos  
- Busca por nome ou código do produto  
- Atualizar estoque (adicionar/remover itens)  
- Listar produtos com estoque baixo  
- Paginação automática  
- Painel administrativo do Django  

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
python manage.py makemigrations
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

## Documentação da API

### Base URL
```
http://localhost:8000/api/
```

### Endpoints

#### 1. Listar Produtos
```
GET /api/produtos/
```

Retorna lista paginada de todos os produtos.

**Exemplo com curl:**
```bash
curl http://localhost:8000/api/produtos/
```

**Buscar produtos:**
```bash
curl http://localhost:8000/api/produtos/?search=notebook
```

#### 2. Criar Produto
```
POST /api/produtos/
```

**Exemplo:**
```bash
curl -X POST http://localhost:8000/api/produtos/ \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Notebook Dell",
    "codigo": "NB-001",
    "quantidade": 15,
    "preco": "3500.00"
  }'
```

#### 3. Detalhes do Produto
```
GET /api/produtos/{id}/
```

**Exemplo:**
```bash
curl http://localhost:8000/api/produtos/1/
```

#### 4. Atualizar Produto
```
PUT /api/produtos/{id}/
PATCH /api/produtos/{id}/  # atualização parcial
```

**Exemplo:**
```bash
curl -X PATCH http://localhost:8000/api/produtos/1/ \
  -H "Content-Type: application/json" \
  -d '{"preco": "3200.00"}'
```

#### 5. Deletar Produto
```
DELETE /api/produtos/{id}/
```

**Exemplo:**
```bash
curl -X DELETE http://localhost:8000/api/produtos/1/
```

#### 6. Atualizar Estoque
```
POST /api/produtos/{id}/atualizar_estoque/
```

**Adicionar itens:**
```bash
curl -X POST http://localhost:8000/api/produtos/1/atualizar_estoque/ \
  -H "Content-Type: application/json" \
  -d '{
    "operacao": "adicionar",
    "quantidade": 10
  }'
```

**Remover itens:**
```bash
curl -X POST http://localhost:8000/api/produtos/1/atualizar_estoque/ \
  -H "Content-Type: application/json" \
  -d '{
    "operacao": "remover",
    "quantidade": 5
  }'
```

#### 7. Produtos com Estoque Baixo
```
GET /api/produtos/estoque_baixo/?limite=10
```

Retorna produtos com quantidade menor ou igual ao limite especificado.

**Exemplo:**
```bash
curl http://localhost:8000/api/produtos/estoque_baixo/?limite=5
```

### Estrutura de Resposta - Produto

```json
{
  "id": 1,
  "nome": "Notebook Dell",
  "codigo": "NB-001",
  "quantidade": 15,
  "preco": "3500.00",
  "criado_em": "2026-01-07T10:30:00Z",
  "atualizado_em": "2026-01-07T10:30:00Z"
}
```

## Estrutura do Projeto

```
controle-estoque/
├── manage.py
├── requirements.txt
├── estoque_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── produtos/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    └── urls.py
```

## Observações de Produção

⚠️ **IMPORTANTE:** Esse projeto tá configurado pra desenvolvimento. Se for usar em produção, lembre de:

- Mudar `DEBUG = False` no settings.py
- Trocar a SECRET_KEY por uma segura (use variáveis de ambiente)
- Configurar ALLOWED_HOSTS corretamente
- Usar banco de dados robusto (PostgreSQL)
- Configurar arquivos estáticos e media corretamente
- Adicionar HTTPS
- Implementar autenticação e permissões
- Fazer backup regular do banco

## Licença

MIT - faça o que quiser com o código 😉

