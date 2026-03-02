# %%
import pandas as pd 

"""
Lembre de tratar a serie como um dicionário, pois ela possui chaves e valores.
0 : 10
1 : 20 ...

acessar o ultimo elemento da serie com -1 vai retornar um erro, pois essa chave não existe.
Use iloc para acessar o ultimo elemento da serie, pois ele acessa pelo indice e não pela chave.

series_idades.iloc[-1]

tem como ordenar a serie pelo indice ou pelos valores, mas isso não altera a série original, apenas retorna uma nova série ordenada.


"""

idades = [
    10,20,30,40,50,
    23,34,45,56,67,
    12,23,34,45,56,
    22,33,44,55,66,
    19,29,39,49,59
]

index = [
    'a','b','c','d','e',
    'f','g','h','i','j',
    'k','l','m','n','o',
    'p','q','r','s','t',
    'u','v','w','x','y'
]

series_idades = pd.Series(idades, index=index)



# series_idades.sort_index() 

# series_idades.sort_values()

# series_idades.iloc[-1]

series_idades["u"] # 19 acesando pela chave
series_idades.iloc[0] # 10 acessando pelo indice


# %%
