from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello():
    return{'Hello':'World'}

@app.get('/api/restaurentes/')
def get_restaurentes(restaurente: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurente is None:
            return{'Dados':dados_json}
        
        dados_restaurantes = []
        for item in dados_json:
            if item['Company'] == restaurente:
                dados_restaurantes.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurente':restaurente, 'cardapio': dados_restaurantes}
    else:
        print(response.status_code)