# %%
import pandas as pd
import requests

# %%

df_clientes = pd.read_csv('./data/clientes.csv', sep=',')
df_compras = pd.read_csv('./data/compras.csv', sep=',')

df_clientes.head()
# %%
df_compras.head()
# %%
