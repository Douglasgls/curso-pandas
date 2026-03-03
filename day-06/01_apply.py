#%% 
import pandas as pd

cliente = pd.read_csv('../data/transacoes.csv',sep=';')

cliente.head()
# %%
# Jeito feio de se fazer 
id_novo = [str(clienteID).split("-")[-1] for clienteID in cliente["IdCliente"]]
cliente["id_novo"] = id_novo
cliente.head()
# %%

# FORMA MAIS USADA 
def get_last_id(x:str):
    return x.split("-")[-1]

cliente["IdCliente"].apply(get_last_id)
# %%