# %%

# Deu errado pois estou recebendo o erro 403 Forbidden, provavelmente por conta do bloqueio do site.
import pandas as pd 

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
dfs
# %%
