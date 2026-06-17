from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get('/api/hello')
def hello_world():
    
    '''
    
    Endpoint para retornar uma mensagem de boas-vindas.
    
    '''
    return {'message': 'Hello World!'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    
    Endpoint para retornar o cardápio de um restaurante específico ou todos os restaurantes disponíveis.
    
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()

        # Se restaurante não for informado, retorna todos agrupados
        if restaurante is None:
            dados_restaurante = {}
            for item in dados_json:
                nome = item['Company']
                if nome not in dados_restaurante:
                    dados_restaurante[nome] = []
                dados_restaurante[nome].append({
                    "Item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
            return {'Cardapio': dados_restaurante}

        # Se um restaurante for especificado, filtrar utilizando busca genérica (case-insensitive)
        else:
            itens_restaurante = []
            for item in dados_json:
                if restaurante.lower() in item['Company'].lower():
                    itens_restaurante.append({
                        "Item": item['Item'],
                        "price": item['price'],
                        "description": item['description']
                    })
            return {'Restaurante': restaurante, 'Cardapio': itens_restaurante}
    else:
        return {'Erro': f'Erro ao fazer a requisição: {response.status_code} - {response.text}'}
# Abrir o terminal e executar o comando abaixo para rodar o servidor FastAPI    
# uvicorn main:app --reload

  