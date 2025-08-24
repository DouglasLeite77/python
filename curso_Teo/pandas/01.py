# %%
import pandas as pd
# %%

df = pd.read_csv("clientes.csv", sep =";")
# %%
df.head(n=10)

# %%
df.tail()
# %%
df.sample(10)
# %%
df.shape
# %%
df.columns
# %%
df.info()
# %%
df = df.rename(columns={"QtdePontos":"qtPontos"})
df.rename(columns={"QtdePontos":"qtPontos"}, inplace=True)
# %%
df.head()
# %%
colunas = df.columns.tolist()
colunas.sort()
colunas
# %%
df[colunas]
# %%
