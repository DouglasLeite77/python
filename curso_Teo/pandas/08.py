# %%
import pandas as pd
import sqlalchemy as sqal

with open("etl.sql") as open_file:
    query = open_file.read()

print(query)
# %%


engine = sqal.create_engine("sqlite:///./database.db")

# %%

cliente = pd.read_sql_table(table_name="clientes", con=engine)
# %%
cliente
# %%
