# %%
import pandas as pd
# %%

df= pd.read_csv("./clientes.csv", sep=';')
df.head()
# %%
df['DtCriacao'] = df['DtCriacao'].apply(lambda x: ' '.join(x.split(' ')[:2]))
df['DtCriacao'].head()

# %%
df['DtCriacao'] = df['DtCriacao'].apply(lambda x: x.split('.')[0])
# %%

pd.to_datetime(df['DtCriacao'])
# %%
df['DtCriacao']
# %%
