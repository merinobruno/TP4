import pandas as pd

# 1) Concatenar dos dataframes
df1 = pd.read_csv('argentina_cars1.csv')
df2 = pd.read_csv('argentina_cars2.csv')
mi_df = pd.concat([df1, df2], axis=0)
print(mi_df)