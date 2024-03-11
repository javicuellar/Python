# 04_Pandas_Funciones_Avanzadas_Data_Science

 - Sacado de Advanced Pandas Functions for Data Analysis
    https://thecleverprogrammer.com/2024/02/27/advanced-pandas-functions-for-data-analysis/

1) GroupBy
GroupBy permite agrupar filas que comparten el mismo valor en una o varias columnas y, a continuación, realizar una operación en cada grupo. Puede ser cualquier cosa, desde la agregación (por ejemplo, suma, media) hasta la transformación (por ejemplo, la estandarización de datos dentro de un grupo) o la filtración (por ejemplo, la eliminación de datos que no cumplen una determinada condición).

Use GroupBy para segmentar el conjunto de datos en grupos y aplicar cálculos para cada grupo por separado, como resumir los datos de ventas por región o calcular las puntuaciones medias por grupos de alumnos.

2) Tablas dinámicas
Una tabla dinámica es una herramienta de resumen de datos que se utiliza con frecuencia en el procesamiento de datos. Pandas pivot_table puede ordenar, contar y sumar automáticamente los datos almacenados en un DataFrame o Series y es particularmente útil para resumir rápidamente los datos y resaltar aspectos importantes.

Use pivot_table cuando necesite crear una tabla dinámica de estilo hoja de cálculo como DataFrame. Es especialmente útil para resumir y analizar datos para ver comparaciones, patrones y tendencias en los datos.

3) Indexación múltiple
Pandas admite la indexación multinivel, o indexación jerárquica, que le permite almacenar y manipular datos con un número arbitrario de dimensiones en estructuras de datos de dimensiones inferiores como Series (1D) y DataFrame (2D).

Utilice la indización múltiple cuando necesite trabajar con datos que se pueden clasificar por dos o más claves por punto de datos. Es especialmente útil para agrupar datos en categorías y subcategorías.

4) Fusión, unión y concatenación
Estas funciones se utilizan para combinar diferentes DataFrames. Merge es para combinar datos en columnas o índices, Join es para combinar datos en una columna clave o un índice, y Concat es para anexar tramas de datos una debajo de la otra o una al lado de la otra.

Use merge cuando necesite combinar columnas al estilo de una base de datos, use join para combinar datos en un índice o columna clave y use concat para apilar DataFrames vertical u horizontalmente.

5) Transformación de datos con apply() y map()
apply() le permite aplicar una función a lo largo de un eje del DataFrame o en una Serie. map() es un método de serie que se utiliza para sustituir cada valor de una serie por otro valor.

Use apply() para aplicar una función a través de filas/columnas de un DataFrame o en una Serie, y use map() para transformaciones y sustituciones de elementos en una Serie.

6) Función de consulta
La función query() de Pandas permite filtrar un DataFrame utilizando una expresión de consulta pasada como una cadena. Este método ofrece una sintaxis más legible para filtrar datos en comparación con la indexación booleana tradicional, especialmente para condiciones complejas. Puede ser especialmente útil cuando se trabaja con DataFrames de gran tamaño y se realizan operaciones de filtrado de datos dinámicos.

Utilice la función query() cuando necesite realizar operaciones de filtrado en un DataFrame y prefiera una sintaxis concisa y legible. Es especialmente útil en situaciones en las que las condiciones de filtro son complejas o cuando se construyen dinámicamente cadenas de consulta basadas en la entrada del usuario o la lógica del programa.

7) Funcionalidad de series temporales
Pandas proporciona una potente funcionalidad de series temporales para manipular y analizar datos de series temporales. Incluye capacidades para la generación de rangos de fechas, conversión de frecuencia, estadísticas de ventanas móviles, cambio de fechas y retrasos. Estas funciones son esenciales para trabajar con datos financieros, económicos, ambientales y muchos otros tipos de datos que están indexados por tiempo.

Utilice la funcionalidad de serie temporal de Pandas cuando trabaje con datos indexados por tiempo y necesite realizar operaciones como:
  - Remuestreo para diferentes frecuencias de tiempo (por ejemplo, convertir datos de minutos en datos de 5 minutos).
  - Rellenar las fechas y horas que faltan en una serie temporal.
  - Valores cambiantes o rezagados para el análisis de series temporales.
  - Calcular las estadísticas de la ventana móvil o móvil (por ejemplo, la media móvil).
  - Trabajar con zonas horarias.