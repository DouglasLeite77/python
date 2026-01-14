# %%
import pandas as pd
from pandasql import sqldf
# %%

df = pd.read_csv("./data/points_tmw - dados origem.csv")
df.head()
# %%
media = df['qtdPontos'].mean()
media
# %%
mediana =   df['qtdPontos'].median()
mediana
# %%
minimo = df['qtdPontos'].min()
maximo = df['qtdPontos'].max()
minimo
maximo
# %%
quartil_1 = df['qtdPontos'].quantile(0.25)
print(quartil_1)
quartil_2 = df['qtdPontos'].quantile(0.50)
print(quartil_2)
quartil_3 = df['qtdPontos'].quantile(0.75)
print(quartil_3)
quartil_4 = df['qtdPontos'].quantile(1)
print(quartil_4)
# %%
df['qtdPontos'].describe()
# %%

usuario = df.groupby('idUsuario').agg({'qtdPontos':'sum', 'idTransacao':'count'}).reset_index()
usuario

# %%

usuario[['idTransacao','qtdPontos']].describe()
# %%
