# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# %%

df = pd.read_csv('./data/points_tmw_dados_origem.csv')
df.head()


# %%

df['DataTransacao'] = pd.to_datetime(df['dtTransacao']).dt.date
df['DataTransacao']

# %%

group_data = df.groupby('DataTransacao').agg({
    'qtdPontos': 'sum',
    'idTransacao': 'count',
}).reset_index()
group_data = group_data.sort_values(by='DataTransacao')
group_data

plt.scatter(x=group_data['qtdPontos'], y=group_data['idTransacao'])
plt.show()
# %%

group = df.groupby("qtdPontos")['idTransacao'].count().reset_index()
group

sns.barplot(x=group['qtdPontos'], y=group['idTransacao'])

# %%

plt.boxplot(group_data['qtdPontos'])

# %%

plt.plot(group_data['DataTransacao'], group_data['idTransacao'])

# %%

df.head()