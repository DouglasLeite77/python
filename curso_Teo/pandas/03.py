# %%
import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {"User-Agent": "Mozilla/5.0"}  # finge ser navegador
response = requests.get(url, headers=headers)

tables = pd.read_html(response.text)

# %%
ufs = tables[1]
# %%

ufs.head()
# %%

def verificação(linha):
    return linha['Abreviação'] == 'AC'


# %%
ufs.apply(verificação, axis=1)
# %%

ufs.apply(lambda x: x['Abreviação'] == 'AC', axis=1)

# %%
