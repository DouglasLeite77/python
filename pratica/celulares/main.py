# %%
import pandas as pd
import pandasql

df = pd.read_csv("./dados_celulares.csv", index_col='Unnamed: 0')
df.head()
df.columns

# %%

df['Percentage Discount'] = df['Percentage Discount'].str.replace("off","").str.replace("%","").str.strip().astype(float)
df.head()


df['Price'] = df['Price'].astype(float)
desconto = df['Price'] * (df['Percentage Discount']/100)
desconto

df.insert(3,'Desconto',desconto)
df.head()

df[['Model Name','Cor']] = df['Model Name'].str.split('(', n=1,expand=True)

df['Cor'] = df['Cor'].str.split(",").str[0]

df['RAM & ROM'] = df['RAM & ROM'].str.replace("RAM",'').str.replace("ROM",'')
split02 = df['RAM & ROM'].str.split('|',n=1, expand=True)
df.insert(6,'RAM',split02[0])
df.insert(7,'ROM',split02[1])
df = df.drop('RAM & ROM', axis=1)
df['Processor'] = df['Processor'].str.removesuffix(" Processor")
df['Battery Capacity'] = df['Battery Capacity'].str.removesuffix(" Battery")
df = df.rename(columns={"Model Name":"Model"})

split03 = df['Display Size'].str.split("(",n=1, expand=True)
df['Display Size'] = split03[0]
df.insert(9,'Display describe', split03[1])
df['Display describe'] = df['Display describe'].str.replace(")",'')

split04 = df['Camera'].str.split("|", n=1, expand=True)

df['Camera'] = split04[0]
df = df.rename(columns={'Camera':'Camera traseira'})
df.insert(11,'Camera frontal',split04[1])
df.head()