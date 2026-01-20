# %%
import pandas as pd

df = pd.read_csv("./dados_celulares.csv", index_col='Unnamed: 0')
df.head()
df.columns
# %%

df['Percentage Discount'] = df['Percentage Discount'].str.replace("off","").str.replace("%","").str.strip().astype(float)
df.head()

# %%
df['Price'] = df['Price'].astype(float)
desconto = df['Price'] * (df['Percentage Discount']/100)
desconto

# %%
df.insert(3,'Desconto',desconto)
df.head()