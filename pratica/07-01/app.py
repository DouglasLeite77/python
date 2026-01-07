# %%
import pandas as pd
from csv import reader
# %%

file = open("./data.csv", encoding='utf-8')
read_file = reader(file)
df = list(read_file)
df
# %%
prio_max = []
for i in df:
    if i[5] == 'Alta' and i[4] == 'Pendente':
        prio_max.append(i)
        
print(prio_max)
len(prio_max)
# %%
bairros = {}
for i in df[1:]:
    
    if i[3] not in bairros:
        bairros[i[3]] = 1
    else:
        bairros[i[3]] = bairros[i[3]] + 1
        
print(bairros)

# %%

for i in df[1:]:
    i[6] = i[6].replace("R$", "")
    i[6] = float(i[6])

# %%
df
# %%
def analisar_custo_bairro(lista,bairro):
    soma = 0
    for i in lista:
        if i[3] == bairro:
            soma += i[6]
    print(soma)
    
# %%
analisar_custo_bairro(df,'Brasil')
# %%
df[0].append("categoria_invertimento")

for i in df[1:]:
    match i:
        case i if i[6] < 500:
            i.append("Investimento Baixo")
        case  i if i[6] > 500 and i[6] <= 2000:
            i.append("Investimento Médio")
        case  i if i[6] > 2000:
            i.append("Investimento Alto")
        
# %%
df
# %%
