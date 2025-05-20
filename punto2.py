import pandas as pd

# 2) Filtrar el nuevo DataFrame para obtener solo las filas donde una el valor del
# vehículo sea mayor a 3000000 y menor a 5000000, sea marca Volkswagen, sea modelo mayor
# a 2017 y sea de color blanco. Guardar este nuevo dataframe en un nuevo archivo .csv

df1 = pd.read_csv('argentina_cars1.csv')
df2 = pd.read_csv('argentina_cars2.csv')
mi_df = pd.concat([df1, df2], axis=0)

mi_df2 = mi_df[(mi_df['money'] > 3000000) & (mi_df['money'] < 5000000) &
               (mi_df['brand'] == 'Volkswagen') & (mi_df['model'] > '2017') &
               (mi_df['color'] == 'Blanco')]
mi_df2.to_csv('mi_df2.csv', index=False, header=True)
print(mi_df2)