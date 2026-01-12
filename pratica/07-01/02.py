# %%
import pandas as pd
import csv
df = pd.read_csv("./contratos.csv")
df

# %%
file = open("./contratos.csv", encoding='utf-8')
file_read = csv.reader(file)
dfcsv = list(file_read)
dfcsv.remove(dfcsv[-1])
dfcsv.remove(dfcsv[-3])

# %%
for i in dfcsv[1:]:
    i[4] = i[4].replace("R$", "").replace(".","").strip()
    i[4] = float(i[4])
# %%
dic = {}
for i in dfcsv[1:]:
    if i[-1] in dic:
        dic[i[-1]] += i[4]
    else:
        dic[i[-1]] = i[4]
# 
for i in dfcsv:
    print(i)

# %%

df['valor_contrato'] = df['valor_contrato'].replace("R$", "").replace(".","").astype(float)
df['valor_contrato']

# %%

df['tipo_empresa'] = df['fornecedor'].apply(lambda x: "Grande Empresa" if "S.A" in x.upper() or "LTDA" in x.upper() else 'Outros' )
df.head()
# %%
df['data_assinatura'] = pd.to_datetime(df['data_assinatura'], format='mixed')

# %%
relatorio = df.groupby('fiscal').agg(total = ('valor_contrato', 'sum'), media = ('valor_contrato', 'mean'), qtd = ('valor_contrato', 'count'))
relatorio
# %%
