# %%
import pandas as pd

df = pd.DataFrame({
    "nome": ["Julia","Julia","Jorge", "Melissa","Lucas"],
    "sobrenome": ["Silva","Silva","Santos","Calvo", "Calvo"],
    "salario": [1213,1234,4312,1232,9001]
})
# %%
df = (df.sort_values("salario", ascending=False)
      .drop_duplicates(subset=["nome", "sobrenome"])
      )
df
# %%
