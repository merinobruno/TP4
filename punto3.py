import pandas as pd

df1 = pd.read_csv('argentina_cars1.csv')
df2 = pd.read_csv('argentina_cars2.csv')
mi_df = pd.concat([df1, df2], axis=0)

# 3) Seleccionar las columnas “brand”, “model” y “kilometres”. Luego armar un nuevo
# dataframe con todos los autos que tengan más de 10000 kilómetros.
mi_df3 = mi_df.loc[:, ['brand', 'model', 'kilometres']]
mi_df3 = mi_df3[mi_df3['kilometres'] > 10000]
print(mi_df3)