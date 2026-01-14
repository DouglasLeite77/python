# %%
import pandas as pd
from pandasql import sqldf

df= pd.read_csv("./data/points_tmw_dados_origem.csv")
df.describe()
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

query = """
SELECT * FROM df
"""
result = sqldf(query, locals())
result

# %%

query = """
with tb_subquery as (
SELECT qtdPontos from df
order by qtdPontos
limit 1 + (select count(*) % 2 == 0 FROM df)
offset 2500
),
mediana as (
SELECT AVG(qtdPontos) FROM tb_subquery
),
medias as (
    SELECT AVG(qtdPontos) FROM df
),
tb_quartil01 as (
    SELECT qtdPontos from df
    order by qtdPontos
    limit 1 + (select count(*) % 2 == 0 FROM df)
    offset (select 1 * count(*) / 4 from df)
),
quartil01 as (
    SELECT AVG(qtdPontos) from tb_quartil01
),
tb_quartil02 as (
    SELECT qtdPontos from df
    order by qtdPontos
    limit 1 + (select count(*) % 2 == 0 FROM df)
    offset (select 2 * count(*) / 4 from df)
),
quartil02 as (
    SELECT AVG(qtdPontos) from tb_quartil02
),
tb_quartil03 as (
    SELECT qtdPontos from df
    order by qtdPontos
    limit 1 + (select count(*) % 2 == 0 FROM df)
    offset (select 3 * count(*) / 4 from df)
),
quartil03 as (
    SELECT AVG(qtdPontos) from tb_quartil03
),
min as (
    SELECT min(qtdPontos) FROM df
),
max as (
    SELECT MAX(qtdPontos) FROM df
)
SELECT * FROM medias, min, quartil01,quartil02,quartil03,max
"""

resp = sqldf(query, locals())
resp

