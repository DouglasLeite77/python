# %%
import pandas as pd
# %%
clientes = pd.read_csv("./clientes.csv", sep=";")
# %%
clientes.head()
clientes.describe()
clientes.dtypes
# %%
filtro = (clientes.dtypes == "object")
# %%

clientes.dtypes[filtro]
# %%

x = clientes.dtypes[~filtro].index.tolist()
# %%

clientes[x].mean()
# %%
clientes[x].describe()
# %%
clientes = clientes[clientes['QtdePontos'] > 100]
# %%
clientes.head()
# %%