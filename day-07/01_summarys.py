# %% 
import pandas as pd

idades = [10, 20, 30, 40, 50]
idades_series = pd.Series(idades)
idades_series.sum()
idades_series.mean()
idades_series.median()
idades_series.std()
idades_series.describe()

# %% 
clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.dtypes

num_columns = clientes.dtypes[(clientes.dtypes == "int64")].index.to_list()
clientes[num_columns].describe()
# %%
