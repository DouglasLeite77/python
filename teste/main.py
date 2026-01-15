# %%
import pandas as pd
from pandasql import sqldf

# %%

clientes = pd.read_csv("./data/clientes.csv", encoding='UTF-8')
itens_pedidos = pd.read_csv("./data/itens_pedido.csv")
pedidos = pd.read_csv("./data/pedidos.csv", encoding='UTF-8')
produtos = pd.read_csv("./data/produtos.csv")

clientes['cidade'] = clientes["cidade"].replace("sao Paulo","São Paulo").replace("Sao Paulo","São Paulo").replace("Rio","Rio de Janeiro")

# %%

query = """
SELECT p.status,grupo, sum(valor_total) as total,count(status) as qtd FROM clientes c
left join pedidos p on c.cliente_id = p.cliente_id
group by c.grupo, p.status
order by p.status, qtd desc
"""

result = sqldf(query, locals())
result

# %%

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
order by m.media desc
"""


result = sqldf(query, locals())
result

# %%

query = """
SELECT cidade, sum(valor_total) as total
from clientes c
left join pedidos p on c.cliente_id = p.cliente_id
WHERE status = "Confirmado"
group by cidade
order by total desc
"""
result = sqldf(query, locals())
result


# %%

query = """
SELECT cidade, estado FROM clientes
group by estado
"""

result = sqldf(query, locals())
result

