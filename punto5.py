import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Libreria para el formato de numeros
import matplotlib.ticker as ticker

df1 = pd.read_csv('argentina_cars1.csv')
df2 = pd.read_csv('argentina_cars2.csv')
mi_df = pd.concat([df1, df2], axis=0)

# 5) Leer un archivo .csv producto de la unión de argentina_cars1.csv
# argentina_cars2.csv y combinar un gráfico de barras con un gráfico de líneas utilizando
# matplotlib o seaborn.
mi_df.to_csv('argentina_cars_concat.csv', index=False, header=True)
mi_df4 = pd.read_csv('argentina_cars_concat.csv')
valor_promedio = mi_df4['money'].mean()
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

# grafico de barras de precio promedio por marca
sns.lineplot(data=mi_df4, x='year', y='money', hue='brand')
plt.title('Precio promedio por marca')
plt.xlabel('Año')
plt.ylabel('Precio promedio')
plt.xticks(rotation=45)
plt.grid()
plt.show()
