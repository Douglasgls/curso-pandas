#%% 
import pandas as pd 



#%%

pontos = [10,1,100,50,30,90,80,50,30,70]
filtros = []

resultado = []
for i in pontos:
    filtros.append(i >=50)


for i in range(len(pontos)):
    if filtros[i]:
        resultado.append(pontos[i])
resultado

# %%

import datetime 

df = pd.read_csv('../data/transacoes.csv', sep=";")
df.head()

# valores maior que 50 e menor que 100 
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100) 
df[filtro]

# %%
