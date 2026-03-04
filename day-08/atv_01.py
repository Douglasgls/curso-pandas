# %% 

# quem teve mais streak ? 

import pandas as pd
transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()
# %%
transacoes_prod = pd.read_csv("../data/transacao_produto.csv", sep=";")
transacoes_prod.head()
# %%
produto = pd.read_csv("../data/produtos.csv", sep=";")
produto.head()
# %%
cliente_transacao_produto =  transacoes.merge(
    right=transacoes_prod,
    how="left",
    on=["IdTransacao"],
)

cliente_transacao_produto[["IdCliente","IdTransacao","IdProduto"]]

# %%
df_full = cliente_transacao_produto.merge(
    right=produto,
    how="left",
    on=["IdProduto"],
)

df_full = df_full[df_full["DescNomeProduto"] == "Presença Streak"]

df_full

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)

# %%

# FORMA MAIS USADA 
unico_produto = produto[produto["DescNomeProduto"] == "Presença Streak"]

(
    transacoes.merge(right=transacoes_prod,how="left",on=["IdTransacao"])
              .merge(right=unico_produto, how="right", on="IdProduto")
              .groupby(by=["IdCliente"])["IdTransacao"]
              .count()
              .sort_values(ascending=False)
              .head(1)
)
# %%
