#%% 
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
# %%

df["qtdePontos"] + 100

# %%