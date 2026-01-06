WITH freq_abs as (
SELECT descProduto, count(idTransacao) as qtd from points GROUP BY descProduto
),
freq_abd_acum as (
    SELECT *, sum(qtd) OVER (ORDER BY descProduto) as freq_abs_acum from freq_abs
),
freq_rel as (
    SELECT *, 100.00 * qtd / (SELECT sum(qtd) from freq_abs) as freq_rel from freq_abd_acum GROUP BY descProduto
),
freq_rel_acum as (
    SELECT *, sum(freq_rel) OVER (ORDER BY descProduto) as freq_rel_acum from freq_rel
)
SELECT * from freq_rel_acum





