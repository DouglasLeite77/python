# %%
import pandas as pd
import pandasql

# %%

clientes = pd.read_csv("./data/clientes.csv")
itens_pedidos = pd.read_csv("./data/itens_pedido.csv")
pedidos = pd.read_csv("./data/pedidos.csv")
pd.read_csv("./data/produtos.csv")