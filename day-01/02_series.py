# %% 

import pandas as pd 


idades = [
    10,20,30,40,50,
    23,34,45,56,67,
    12,23,34,45,56,
    22,33,44,55,66,
    19,29,39,49,59
]

series_idades = pd.Series(idades)

series_idades.describe()

# %%
