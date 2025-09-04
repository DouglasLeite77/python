# %%
import pandas as pd
# %%

df = pd.read_csv("./transacoes.csv", sep=";")
# %%


df.groupby(by="IdCliente").count()[["QtdePontos"]]
# %%

summary = df.groupby(by=["IdCliente"], as_index=False).agg({"IdTransacao": ["count"], "QtdePontos": ["sum", "mean"]})
# %%

