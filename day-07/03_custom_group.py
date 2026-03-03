# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.columns
# %%

def life_time(x:pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days


summery = (transacoes.groupby(by=["IdCliente"], as_index=False)
           .agg(
               {
                   "IdTransacao": ["count"],
                   "QtdePontos": ["sum","mean"],
                   "DtCriacao": [life_time]
               }
           )
           )

summery.head()

# %%
