# %% 
import pandas as pd
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes.head()

# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes
# %%

#  usei o left_on e right_on para especificar as colunas de cada tabela que serão usadas para o merge
transacoes.merge(right=clientes,
                 left_on="IdCliente", 
                 right_on="idCliente",
                 how="right",
                 suffixes=["Transacao","Cliente"]
                )
# %%
