# %%
import pandas as pd
import sqlalchemy 

with open("etl.sql") as open_file:
    query = open_file.read()

print(query)
# %%
