# %%
import pandas as pd

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

transacoes.head()
# %%
transacoes = transacoes.sort_values("DtCriacao")
transacoes
# %%