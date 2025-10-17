# %%
import pandas as pd
# %%

df = pd.read_csv('./clientes.csv', sep=";")

df.head()
# %%

series = pd.Series([1,2,3,4,12,123,43,46,87,123])

series.mean()
series.var()
series.describe()
# %%
