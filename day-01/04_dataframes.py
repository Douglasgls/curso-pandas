# %%

import pandas as pd

idades = [
    10,20,30,40,50,
    23,34,45,56,67,
    12,23,34,45,56,
    22,33,44,55,66,
    19,29,39,49,59
]

nomes = [
    'a','b','c','d','e',
    'f','g','h','i','j',
    'k','l','m','n','o',
    'p','q','r','s','t',
    'u','v','w','x','y'
]

series_idades = pd.Series(idades)

series_pandas = pd.Series(nomes)

# %% 
 
df = pd.DataFrame()
df['idades'] = series_idades
df['nomes'] = series_pandas

# %% 

df["idades"]

df.iloc[0]  # acessa a primeira linha do dataframe
# %%

