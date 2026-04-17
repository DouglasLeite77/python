# %%
import pandas as pd
import requests

# %%

df_clientes = pd.read_csv('./data/clientes.csv', sep=',', dtype={'cep': str})
df_compras = pd.read_csv('./data/compras.csv', sep=',')

df_clientes.head()
# %%
df_compras.head()
# %%

def consulta_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    dados = requests.get(url)
    return dados.json()
# %%

def get_dados():
    lista_ceps = df_clientes['cep'].astype(str).replace(',', '', regex=True)
    
    dados = []
    
    for i in lista_ceps:
        dados.append(consulta_cep(i))
    
    df_dados = pd.DataFrame(dados)
    df_clientes['logradouro'] = df_dados['logradouro']
    df_clientes['bairro'] = df_dados['bairro']
    df_clientes['localidade'] = df_dados['localidade']
    df_clientes['uf'] = df_dados['uf']
# %%

get_dados()
df_clientes.head()
# %%