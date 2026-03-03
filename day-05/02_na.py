# %% 
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes
df = pd.DataFrame({
    "nome": ["Douglas",None,"Jorge"],
    "idade": [None,22, None],
    "salario": [12000,2000,None]
})

df.dropna(how="all", subset=["idade"])

# %%

df["idade"].fillna("DG")
#  %%
