# 1) GroupBy
#
#    GroupBy permite agrupar filas que comparten el mismo valor en una o varias columnas y, a continuación, realizar una
# operación en cada grupo. Puede ser cualquier cosa, desde la agregación (por ejemplo, suma, media) hasta la transformación
# (por ejemplo, la estandarización de datos dentro de un grupo) o la filtración (por ejemplo, la eliminación de datos que no
# cumplen una determinada condición).
#    Use GroupBy para segmentar el conjunto de datos en grupos y aplicar cálculos para cada grupo por separado, como resumir
# los datos de ventas por región o calcular las puntuaciones medias por grupos de alumnos.
import pandas as pd

# sample dataframe
df = pd.DataFrame({
    'A': ['Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'B': [1, 2, 3, 4],
    'C': [2.0, 5., 8., 1.]
})

print("Dataframe origen:\n", df)
print("\n")

# grouping by column 'A' and summing up the other columns
grouped = df.groupby('A').sum()

print("Dataframe agrupado por columna A:\n", grouped)
print("\n\n")

# 2) Tablas dinámicas

#   Una tabla dinámica es una herramienta de resumen de datos que se utiliza con frecuencia en el procesamiento de datos. 
# Pandas pivot_table puede ordenar, contar y sumar automáticamente los datos almacenados en un DataFrame o Series y es
# particularmente útil para resumir rápidamente los datos y resaltar aspectos importantes.
#   Use pivot_table cuando necesite crear una tabla dinámica de estilo hoja de cálculo como DataFrame. Es especialmente útil
# para resumir y analizar datos para ver comparaciones, patrones y tendencias en los datos.
import numpy as np

pivot = pd.pivot_table(df, values='C', index=['A'], aggfunc=np.sum)
print("Dataframe tabla dinamica (pivot_table):\n", pivot)
print("\n\n")


# 3) Indexación múltiple

#    Pandas admite la indexación multinivel, o indexación jerárquica, que le permite almacenar y manipular datos con un número
# arbitrario de dimensiones en estructuras de datos de dimensiones inferiores como Series (1D) y DataFrame (2D).
#    Utilice la indización múltiple cuando necesite trabajar con datos que se pueden clasificar por dos o más claves por punto
# de datos. Es especialmente útil para agrupar datos en categorías y subcategorías.

# creating a dataframe with multi-index
index = pd.MultiIndex.from_tuples([('Delhi', 'one'), ('Delhi', 'two'),
                                   ('Mumbai', 'one'), ('Mumbai', 'two')],
                                  names=['first', 'second'])
df_multi = pd.DataFrame(np.random.randn(4, 2), index=index, columns=['A', 'B'])
print("Indexación múltiple:\n", df_multi)
print("\n\n")


# 5) Transformación de datos con apply() y map()
#    apply() le permite aplicar una función a lo largo de un eje del DataFrame o en una Serie. map() es un método de serie que
# se utiliza para sustituir cada valor de una serie por otro valor.
#    Use apply() para aplicar una función a través de filas/columnas de un DataFrame o en una Serie, y use map() para
# transformaciones y sustituciones de elementos en una Serie.

# using apply()
df['B*2'] = df['B'].apply(lambda x: x * 2)
print("Dataframe B\n", df['B'], "\nEjemplo apply\Dataframe B*2\n",df['B*2'])
print("\n")

# using map() for a Series
df['A_map'] = df['A'].map({'Delhi': 'New Delhi', 'Mumbai': 'Bombay'})
print("Dataframe A\n", df['A'], "\nEjemplo map\nDataframe A_map\n", df['A_map'])
print("\n\n")


# 6) Función de consulta
#    La función query() de Pandas permite filtrar un DataFrame utilizando una expresión de consulta pasada como una cadena.
# Este método ofrece una sintaxis más legible para filtrar datos en comparación con la indexación booleana tradicional,
# especialmente para condiciones complejas. Puede ser especialmente útil cuando se trabaja con DataFrames de gran tamaño y se
# realizan operaciones de filtrado de datos dinámicos.
#    Utilice la función query() cuando necesite realizar operaciones de filtrado en un DataFrame y prefiera una sintaxis concisa
# y legible. Es especialmente útil en situaciones en las que las condiciones de filtro son complejas o cuando se construyen
# dinámicamente cadenas de consulta basadas en la entrada del usuario o la lógica del programa.

import pandas as pd

# sample dataframe
df = pd.DataFrame({
    'A': range(1, 6),
    'B': range(10, 60, 10),
    'C': ['Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi']
})

# using query() to filter rows
filtered_df = df.query('(A > 2) & (C == "Delhi")')

print("Dataset origen:\n", df)
print("\n")
print("Ejemplo Query, filtrado datos A > 2 y datos C = Delhi:\n", filtered_df)