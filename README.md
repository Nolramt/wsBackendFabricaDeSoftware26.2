# Workshop de Backend — Fábrica de Software 26.2

Projeto classificatório desenvolvido em Django + Django REST Framework, com consumo da [Rick and Morty API](https://rickandmortyapi.com/) para busca de Personagens, Localizações e Episódios, além de um sistema de favoritos organizados por pastas, persistidos em banco de dados relacional.

## Funcionalidades

- **Consumo de API externa** (Rick and Morty API) com tratamento de erros via `try/except` e status codes (`200`, `404`, `502`, `503`)
- **Busca por nome** de Personagens, Localizações e Episódios, com páginas HTML dedicadas para cada categoria
- **Sistema de favoritos**: qualquer resultado da busca externa pode ser salvo no banco local
- **Organização por pastas**: os favoritos são vinculados a uma `Pasta` (relacionamento por chave estrangeira), permitindo agrupar itens salvos
- **CRUD completo dos favoritos** (GET, POST, PUT, PATCH, DELETE) via Django REST Framework
- **Documentação da API** gerada automaticamente com drf-spectacular (Swagger UI e Redoc)

## Tecnologias utilizadas

- Django 6.1
- Django REST Framework 3.18.0
- drf-spectacular 0.30.0 (documentação OpenAPI/Swagger)
- requests (consumo de API externa)
- SQLite (banco de dados)

## Estrutura do projeto

```
projeto_fabrica/       → configurações principais do Django (settings, urls)
app/
├── api/
│   ├── viewsets.py     → ViewSets de busca externa e de favoritos (CRUD)
│   ├── serializers.py  → Serializers de validação e persistência
│   └── urls.py
├── models.py           → Personagem/Localização/Episódio favoritos + Pasta
├── views.py             → Views de busca HTML e de favoritar
├── templates/            → Templates HTML de busca por categoria
└── admin.py
```

## Modelo de dados

- `PastaFavoritos` — pasta usada para organizar os favoritos
- `PersonagemFav`, `LocalizacaoFav`, `EpisodioFav` — cada um relacionado a uma `PastaFavoritos` por chave estrangeira (`ForeignKey`)

## Como rodar o projeto

1. Clone o repositório e entre na pasta do projeto:
```bash

git clone <url-do-repositorio>
cd wsBackendFabricaDeSoftware26.2

```

2. Crie e ative um ambiente virtual:
```bash

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash

pip install -r requirements.txt

```

4. Aplique as migrações:
```bash

python manage.py migrate

```

5. Rode o servidor:
```bash

python manage.py runserver

```

6. Acesse:
```
http://127.0.0.1:8000/
```

## Principais endpoints

### Busca (consumo da API externa)
| Rota | Descrição |
|---|---|
| `GET /personagem/?nome=` | Busca personagens por nome |
| `GET /localizacao/?nome=` | Busca localizações por nome |
| `GET /episodio/?nome=` | Busca episódios por nome |

### Favoritar (a partir da busca)
| Rota | Descrição |
|---|---|
| `POST /favoritar-personagem/` | Salva um personagem como favorito |
| `POST /favoritar-localizacao/` | Salva uma localização como favorita |
| `POST /favoritar-episodio/` | Salva um episódio como favorito |

### CRUD de favoritos (DRF)
| Rota | Métodos |
|---|---|
| `/buscar/favoritos/personagem/` | GET, POST |
| `/buscar/favoritos/personagem/{id}/` | GET, PUT, PATCH, DELETE |
| `/buscar/favoritos/localizacao/` | GET, POST |
| `/buscar/favoritos/localizacao/{id}/` | GET, PUT, PATCH, DELETE |
| `/buscar/favoritos/episodio/` | GET, POST |
| `/buscar/favoritos/episodio/{id}/` | GET, PUT, PATCH, DELETE |
| `/buscar/favoritos/pastas/` | GET, POST |
| `/buscar/favoritos/pastas/{id}/` | GET, PUT, PATCH, DELETE |

### Documentação
| Rota | Descrição |
|---|---|
| `/api/schema/swagger-ui/` | Documentação interativa (Swagger UI) |
| `/api/schema/redoc/` | Documentação (Redoc) |