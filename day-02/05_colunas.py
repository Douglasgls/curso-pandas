#%% 
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")

#%% 
df.shape

#%%
df.dtypes


# %%
df = df.rename(columns={"QtdePontos": "qtpontos", "DescSistemaOrigem": "descsistemaorigem"})
df 

# %%
elementos = ["IdCliente","DtCriacao"]
df[elementos]
# %%
