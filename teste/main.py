# %%
import pandas as pd
from pandasql import sqldf

# %%

clientes = pd.read_csv("./data/clientes.csv", encoding='UTF-8')
itens_pedido = pd.read_csv("./data/itens_pedido.csv", encoding='UTF-8')
pedidos = pd.read_csv("./data/pedidos.csv", encoding='UTF-8')
produtos = pd.read_csv("./data/produtos.csv", encoding='UTF-8')

# %%
estados = {
    'São Paulo': 'SP',
    'Maranhão': 'MA',
    'Rio de Janeiro': 'RJ',
    'Belo Horizonte': 'MG',
    'Curitiba': 'PR',
    'Goiânia': 'GO'
}
clientes['cidade'] = clientes["cidade"].replace("sao Paulo","São Paulo").replace("Sao Paulo","São Paulo").replace("Rio","Rio de Janeiro").replace("Goiania",'Goiânia').replace('Maranhao','Maranhão')
clientes['estado'] = clientes['cidade'].map(estados)
produtos['categoria'] = produtos['categoria'].replace("Decoraçao",'Decoração').replace('Eletronicos','Eletrônicos')
# %%

# Receita total e porcentagem agrupada por grupo e por status

query = """
SELECT p.status,grupo, sum(valor_total) as total,count(status) as qtd, round(count(*) * 100.0 / sum(count(*)) over (partition by grupo),2)|| '%' as porcentagem FROM clientes c
left join pedidos p on c.cliente_id = p.cliente_id
group by c.grupo, p.status
order by p.status, qtd desc
"""

resultado = sqldf(query, locals())
resultado

# %%

#Ticket média por grupo

query= """
SELECT 
c.grupo,
AVG(p.valor_total) as ticket_medio
FROM clientes c
JOIN pedidos p ON c.cliente_id = p.cliente_id
where status = 'Confirmado'
GROUP BY c.grupo;
"""

resultado = sqldf(query, locals())
resultado

# %%

#Média e mediana da receita e quantidade de pedidos por estado

query = """
with media as (
SELECT c.estado, ROUND(avg(p.valor_total),2) media, count(p.valor_total) as "qtd pedidos" FROM clientes c
left join pedidos p on c.cliente_id = p.cliente_id
WHERE status = "Confirmado"
group by c.estado
order by media desc
),
ranque as (
SELECT c.estado,
p.valor_total, ROW_NUMBER() OVER (PARTITION BY c.estado ORDER BY p.valor_total) as linha,
COUNT(*) OVER (PARTITION BY c.estado) as total_linhas
from clientes c
left join pedidos p on c.cliente_id = p.cliente_id
WHERE status = "Confirmado"
),
mediana as(
select estado,
AVG(valor_total) AS mediana
FROM ranque
WHERE linha IN (FLOOR((total_linhas + 1) / 2), CEIL((total_linhas + 1) / 2))
GROUP BY estado
order by mediana desc
)
select m.*, mediana.mediana from mediana
left join media m on mediana.estado = m.estado
order by mediana desc
"""

resultado = sqldf(query, locals())
resultado

# %%

# Maior valor de venda por estado e cidade

query = """
SELECT cidade, estado, sum(valor_total) as total
from clientes c
left join pedidos p on c.cliente_id = p.cliente_id
WHERE status = "Confirmado"
group by cidade
order by total desc
"""
resultado = sqldf(query, locals())
resultado


# %%

# Porcentagem por status e categoria da quantidade de pedidos feitos

query = """
SELECT p.categoria, status, count(*) as qtd, ROUND(count(*) * 100.0 / sum(count(*)) over (partition by categoria),2) || '%' as porcentagem FROM itens_pedido ip
left join produtos p on ip.produto_id = p.produto_id
left join pedidos on pedidos.pedido_id = ip.pedido_id
group by status,categoria
order by status, qtd desc
"""

resultado = sqldf(query, locals())
resultado

# %%

# Porcentagem do status por quantidade de itens no pedido

query = """
SELECT ip.quantidade, status, count(*) as qtd, ROUND(count(*) * 100.0 / sum(count(*)) over (partition by quantidade),2) || '%' as porcentagem FROM itens_pedido ip
left join produtos p on ip.produto_id = p.produto_id
left join pedidos on pedidos.pedido_id = ip.pedido_id
group by status, quantidade
order by status, qtd desc
"""

resultado = sqldf(query, locals())
resultado

