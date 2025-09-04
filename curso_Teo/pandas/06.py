#  %%
import pandas as pd
# %%

transacao = pd.read_csv("./transacoes.csv", sep=";")
clientes = pd.read_csv("./clientes.csv", sep=";")
produtos = pd.read_csv("./produtos.csv",sep=";")
trancoesProduto = pd.read_csv("./transacao_produto.csv",sep=";")
# %%


transacao.merge(right=clientes, how="left", on=['IdCliente'], suffixes=["transacao", "cliente"])
# %%
produtos.head()
trancoesProduto.head()
# %%


produtos = produtos[produtos['DescProduto'] == "Presença Streak"]

# %%

(transacao.merge(trancoesProduto, on="IdTransacao", how="left").merge(
    produtos, on="IdProduto", how="right").groupby(
        by="IdCliente")['IdTransacao'].count().sort_values(ascending=False)
).head(1)
# %%
