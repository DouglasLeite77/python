# %%
import pandas as pd
from pandasql import sqldf

df= pd.read_csv("./data/points_tmw_dados_origem.csv")
df.describe()

# %%

variancia = df['qtdPontos'].var(ddof=0)
# ddof = população
variancia

# %%
desvioP = df['qtdPontos'].std().round()
desvioP

# %%

amplitude = (df['qtdPontos'].max() - df['qtdPontos'].min())
amplitude

# %%

CV = (desvioP / df['qtdPontos'].mean())
CV
