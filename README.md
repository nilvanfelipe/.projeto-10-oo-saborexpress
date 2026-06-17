# O Sabor — API de Cardápios de Restaurantes

API REST em Python/FastAPI que agrega e disponibiliza cardápios de grandes redes de fast-food. Os dados são consumidos de uma fonte externa e servidos por endpoints simples.

---

## Contexto de Aprendizado

Este projeto foi desenvolvido como exercício de uma aula de **Programação Orientada a Objetos (POO)**, com foco prático em **consumir e expor uma API REST** usando Python e o Antigravity IDE.

O código em si é escrito de forma funcional/procedural — não há classes próprias (`class`) neste projeto. A POO entra aqui de um jeito mais sutil: ao usar o FastAPI, você está o tempo todo trabalhando com **objetos de bibliotecas de terceiros**:

- `app = FastAPI()` cria uma **instância** da classe `FastAPI`, que é o objeto central que organiza rotas, middlewares e documentação automática.
- `Query(None)` também é um objeto, usado para descrever e validar um parâmetro de query.
- Cada `response` retornado por `requests.get(url)` é um objeto com métodos e atributos próprios (`.status_code`, `.json()`, `.text`).

Ou seja: o foco principal da aula foi aprender a **conectar com uma API externa e construir uma API própria**, e a POO aparece como o paradigma por trás das ferramentas usadas — não como código de classes escrito à mão.

### Como o projeto funciona, passo a passo

1. **Coleta (`app.py`)** — faz um `GET` na API pública de restaurantes, recebe uma lista de itens (cada um com `Company`, `Item`, `price`, `description`) e agrupa esses itens por restaurante em um dicionário. Cada restaurante é então salvo em um arquivo `.json` separado.
2. **Exposição (`main.py`)** — cria um servidor FastAPI com dois endpoints: um de verificação (`/api/hello`) e outro (`/api/restaurantes/`) que busca os dados da mesma API externa em tempo real e os retorna formatados, com a opção de filtrar por nome do restaurante.
3. **Consumo** — qualquer cliente HTTP (navegador, `curl`, frontend) pode chamar esses endpoints e receber JSON pronto para uso, sem precisar lidar com o formato bruto da API externa.

Esse fluxo — **buscar dados externos → transformar → servir via API própria** — é a base de boa parte das integrações que você vai encontrar no mercado, e foi o principal aprendizado prático deste exercício.

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
git clone https://github.com/nilvanfelipe/.projeto-10_oo-saborexpress.git
cd ".projeto-10_oo-saborexpress"

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
.projeto-10_oo-saborexpress/
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
