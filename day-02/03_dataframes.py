# %%

import pandas as pd 

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")

# AMOSTRAS
# %%
df_clientes.head()

# %% 
df_clientes.tail()
# %%
df_clientes.sample(10)
# %%
df_clientes.shape

# %%
df_clientes.columns

# %%
df_clientes.info()
