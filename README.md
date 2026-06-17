# O Sabor — API de Cardápios de Restaurantes

API REST em Python/FastAPI que agrega e disponibiliza cardápios de grandes redes de fast-food. Os dados são consumidos de uma fonte externa e servidos por endpoints simples.

---

## Visão Geral

O projeto tem dois scripts independentes:

| Arquivo | Papel |
|---------|-------|
| `app.py` | Coleta os dados da API externa e exporta um JSON por restaurante |
| `main.py` | Servidor FastAPI — expõe os endpoints REST |

---

## Restaurantes Disponíveis

| Restaurante | Itens |
|-------------|-------|
| McDonald's | 329 |
| KFC | 218 |
| Burger King | 190 |
| Taco Bell | 183 |
| Wendy's | 154 |
| Pizza Hut | 74 |

**Total: 1.148 itens de cardápio.**

---

## Requisitos

- Python 3.9+
- Conexão com a internet (para buscar dados da API externa)

---

## Instalação

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd ".projeto - 10 - oo sabor(v2)"

# Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Linux/macOS

# Instale as dependências
pip install -r requirements.txt
```

---

## Como Usar

### 1. Coletar os dados (opcional)

O repositório já inclui os arquivos JSON gerados. Para atualizá-los com dados frescos da API externa:

```bash
python app.py
```

Isso faz um `GET` em `https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json`, agrupa os itens por restaurante e salva um arquivo `<Restaurante>.json` para cada um.

### 2. Iniciar o servidor

```bash
uvicorn main:app --reload
```

O servidor sobe em `http://127.0.0.1:8000`.

---

## Endpoints

### `GET /api/hello`

Endpoint de verificação de saúde.

**Resposta:**
```json
{ "message": "Hello World!" }
```

---

### `GET /api/restaurantes/`

Retorna o cardápio de todos os restaurantes.

**Resposta:**
```json
{
  "Cardapio": {
    "McDonald's": [
      {
        "Item": "Big Mac",
        "price": 32.90,
        "description": "O clássico sanduíche com dois hambúrgueres."
      }
    ],
    "KFC": [ ... ]
  }
}
```

---

### `GET /api/restaurantes/?restaurante=<nome>`

Filtra por restaurante (busca parcial, sem distinção de maiúsculas/minúsculas).

**Exemplo:**
```
GET /api/restaurantes/?restaurante=burger
```

**Resposta:**
```json
{
  "Restaurante": "burger",
  "Cardapio": [
    {
      "Item": "Whopper",
      "price": 29.90,
      "description": "Hambúrguer grelhado com vegetais frescos."
    }
  ]
}
```

---

## Documentação Interativa

O FastAPI gera automaticamente duas interfaces de documentação:

| Interface | URL |
|-----------|-----|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

---

## Estrutura do Projeto

```
.projeto - 10 - oo sabor(v2)/
├── main.py              # Servidor FastAPI (endpoints REST)
├── app.py               # Script de coleta de dados
├── requirements.txt     # Dependências Python
├── McDonald's.json      # Cardápio gerado pelo app.py
├── KFC.json
├── Burger King.json
├── Pizza Hut.json
├── Taco Bell.json
└── Wendy's.json
```

---

## Fonte de Dados

Os dados são obtidos de:

```
https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json
```

Cada item da API externa possui os campos `Company`, `Item`, `price` e `description`. O `app.py` transforma e persiste esses dados localmente.

---

## Dependências Principais

| Pacote | Versão | Papel |
|--------|--------|-------|
| fastapi | 0.115.12 | Framework web |
| uvicorn | 0.34.2 | Servidor ASGI |
| pydantic | 2.11.3 | Validação de dados |
| requests | 2.32.3 | Requisições HTTP |
| starlette | 0.46.2 | Base ASGI do FastAPI |

Lista completa em [`requirements.txt`](requirements.txt).

---

## Limitações Conhecidas

- A API não possui autenticação.
- Os dados em `app.py` são atualizados manualmente; não há agendamento automático.
- Não há testes unitários ou de integração.
- `main.py` faz uma requisição externa a cada chamada ao endpoint `/api/restaurantes/` — não há cache local.
