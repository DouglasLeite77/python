# %%
import pandas as pd
# %%

df = pd.read_csv("./clientes.csv", sep=";")
df.head()
# %%


df.set_index("IdCliente")
# %%
df_stack = df.set_index("IdCliente").stack()
# %%
df_stack = df_stack.reset_index()
# %%
df_stack.set_index(["IdCliente","level_1"]).unstack()
# %%
df_stack.head()
# %%
df_stack.pivot_table(values=0,columns="level_1",index="IdCliente")

# %%
df_stack.columns(["IdCliente","social","valor"])
# %%
