# %%

import pandas as pd
import sqlalchemy

# %%

dados = pd.read_csv("./data/points_tmw - dados origem.csv")


engine = sqlalchemy.create_engine("sqlite:///data/tab.db")
dados.to_sql("points", engine, if_exists="replace", index=False)
# %%

freq = dados.groupby(['descProduto'])[['idTransacao']].count()

freq['Freq. Abs Acum.'] = freq['idTransacao'].cumsum()

freq['Freq Rel.'] = (freq['idTransacao'] / freq['idTransacao'].sum()) * 100

freq['Freq Rel. Acum'] = freq['Freq Rel.'].cumsum()

freq
# %%
freq_descP = dados.groupby(['descCategoriaProduto'])[['idTransacao']].count()

freq_descP['Freq Abs. Acum'] = freq_descP['idTransacao'].cumsum()

freq_descP['Freq Rel'] = (freq_descP['idTransacao'] / freq_descP['idTransacao'].sum()) *  100

freq_descP['Freq Rel. Acum.'] = freq_descP['Freq Rel'].cumsum()

freq_descP
# %%
