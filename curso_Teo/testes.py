# %%
import requests
import json
from tqdm import tqdm

# %%

ceps = [
    "45020300",
    "45020700"
]

dados = []

for i in tqdm(ceps):

    url = f'https://viacep.com.br/ws/{i}/json/'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

# %%

with open('ceps.json', 'w', encoding='utf-8') as file:
    json.dump(dados, file, ensure_ascii=False, indent=4)
# %%

