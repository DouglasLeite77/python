# %%
import pandas as pd
import os
# %%


df = pd.DataFrame({
    "cliente": [1,2,3,4,5,],
    "nome": ["a","b","c","d","e"]
})
df02 = pd.DataFrame({
    "cliente": [6,7,8,9,10],
    "nome": ["f","g","h","i","j"]
})


# %%
pd.concat([df,df02], ignore_index=True)
# %%
df = df.rename(columns={"cliente": "id"})
df.set_index("id")
# %%

def concat(file_name:str):
    df = pd.read_csv(f"./{file_name}.csv", sep=";")
    return df
# %%
file_names = os.listdir("./")

dfs = []

for i in file_names:
    if i.split(".")[1] == "csv":
        i = i.split(".")[0]
        dfs.append(concat(i)) 

# %%
dfs[1].head()

# %%

df_geral = pd.concat(dfs, axis=1).reset_index(drop=True)
# %%
df_geral.head()
# %%
