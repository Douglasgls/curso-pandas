# %% 
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
replace = {"0000-00-00 00:00:00.000":"2025-10-20 10:00:00.000"}

df["DtCriacao"] = pd.to_datetime(
    df["DtCriacao"].replace(replace)
)

# %% 
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

df["DtCriacao"] != 'NaN' 
# %%

