# %%
import pandas as pd 

url = "https://www.todamateria.com.br/siglas-estados-brasileiros/"
dfs = pd.read_html(url)
uf = dfs[0]
uf.dtypes
# %%
