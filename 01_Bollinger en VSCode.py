#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import plotly.express as pl
#%% Importo el archivo SPY
ruta = '/Users/cesar/Desktop/IBT (Python)/SPY.csv'
df = pd.read_csv(ruta)
df.dtypes
#%% Convierto la columna date a fecha, y la convierto en indice
df['date'] = pd.to_datetime(df['date'])
df.set_index('date')
# %%
df['mm30']df['close'].rolling(30)
# %%
