import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)  # Requisição GET para a URL
print(response)

if response.status_code == 200:  # Verifica se a requisição foi bem sucedida
    dados_json = response.json()  # Converte a resposta em JSON
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({"Item": item['Item'], "price": item['price'], "description": item['description']
        })

else:
    print(f'Erro ao fazer a requisição:', {response.status_code})

for nome_do_restaurante, itens in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(itens, arquivo_restaurante, indent=4)
