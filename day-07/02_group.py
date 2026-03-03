# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

# %%
summary = (transacoes.groupby(by=["IdCliente"], as_index=False)
           .agg(
               {
                   "IdTransacao":["count"],
                   "QtdePontos": ["sum","mean"],
               }
           )
           )
summary.columns = ["IdCliente", "qtdTrans", "totalPontos", "avgPontos"]
# %%
