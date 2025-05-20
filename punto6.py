import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

df1 = pd.read_csv('argentina_cars1.csv')
df2 = pd.read_csv('argentina_cars2.csv')
mi_df = pd.concat([df1, df2], axis=0).reset_index(drop=True)

# Grilla
fig, axes = plt.subplots(2, 2, figsize=(18, 14))

# Marco 1
precio_marca = mi_df.groupby('brand', as_index=False)['money'].mean().sort_values('money', ascending=False)
sns.barplot(ax=axes[0,0], x='brand', y='money', data=precio_marca)
axes[0,0].set_title('Precio promedio por Marca')
axes[0,0].set_xlabel('Marca')
axes[0,0].set_ylabel('Precio')
axes[0,0].tick_params(axis='x', rotation=45)
axes[0,0].yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))

# Marco 2
precio_anio = mi_df.groupby('year', as_index=False)['money'].mean()
sns.lineplot(ax=axes[0,1], x='year', y='money', data=precio_anio)
axes[0,1].set_title('Tendencia de Precio por Año')
axes[0,1].set_xlabel('Año')
axes[0,1].set_ylabel('Precio')
axes[0,1].yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,.0f}'))
axes[0,1].grid()

# Marco 3
cantidad_tipo = mi_df['body_type'].value_counts().reset_index()
sns.barplot(ax=axes[1,0], x='count', y='body_type', data=cantidad_tipo)
axes[1,0].set_title('Cantidad de autos por tipo')
axes[1,0].set_xlabel('Cantidad de autos')
axes[1,0].set_ylabel('Tipo de auto')

# Marco 4
distancia_anio = mi_df.groupby('year', as_index=False)['kilometres'].mean()
sns.lineplot(ax=axes[1,1], x='year', y='kilometres', data=distancia_anio)
axes[1,1].set_title('Distancia promedio recorrida por año')
axes[1,1].set_xlabel('Año')
axes[1,1].set_ylabel('Kilometros')
axes[1,1].grid()

plt.show()