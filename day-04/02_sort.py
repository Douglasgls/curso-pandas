#%% 
import pandas as pd
clientes = pd.read_csv("../data/clientes.csv", sep=";")

# %%
clientes.sort_values(by="qtdePontos", ascending=False, inplace=True)
clientes.head(3)
# %%