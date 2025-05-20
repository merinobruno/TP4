import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 4) Leer el archivo mundial.csv, armar un dataframe con selecciones y cantidad de
# mundiales ganados. Luego graficar un histograma.
mundial_df = pd.read_csv('mundial.csv')
mundial_df = mundial_df[['Winners']]
mundial_df = mundial_df[mundial_df['Winners'] > '0']
mundial_df['Wins'] = mundial_df.groupby('Winners')['Winners'].transform('count')
mundial_df = mundial_df.drop_duplicates(subset=['Winners'])

mundial_df = mundial_df.groupby("Winners")['Wins'].mean().sort_values(ascending=False)
plt.bar(mundial_df.index, mundial_df.values, color='blue')
plt.xlabel('Winners')
plt.ylabel('Wins')
plt.title('Mundiales ganados por equipo')
plt.xticks(rotation=45)
plt.show()