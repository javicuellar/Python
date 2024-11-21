# Tareas
========

### TRABAJO
-----------

* GFOR.- Extraer datos de solicitudes (excel) del nuevo modelo.


### Otras
----------

* FOTOS NAS.- Archivar.

* Incluir en los backups directorio NAS_Python


### Python

* Modificar nombre carpeta Python en NAS a NAS_Python, para tenerla en Visual Studio idenificada.

* Alertas.- En alerta_ficheros, analizar como incluir el tamaño de ficheros como parámetro. Y poner fuera del contenedor, en el volumen, para poder modificar automáticamente.
    Poner Alertas como un demonio que se ejecuta cada 5 minutos.

* Llevar el proyecto AppWeb Finanzas a Github.

* AppWeb Finanzas, realizar cálculos en los módulos y grabar en SQLite (actualizar cada 5 min.).
    - En web sólo lée de SQLite y muestra la información.
    - Visualización cartera:
        * Falta diferencia -> saber si aumenta o disminuye, dato mensual, semanal, diario.
        * Resumen agrupado por producto -> Diferencia, precio, precio anterior
        * Quitar columnas a mostrar (simplificar) -> Ticker, Entidad, producto, Num., Tipo Act.
            Coger sólo columnas -> Descripción, Dif, Precio, P. Ant.
        * Cartera completa (resumen) -> Zoom: Acciones, ETFs, P. Pensiones, Cuentas.


### FINANZAS

* Incluir datos de hipoteca del 2.022 en movimientos.
* Pruebas movimientos en varias hojas y unirlas en excel Informe (Anexar consultas)
    * Unir SALDOS, para llevarlos de una hoja a otra -> fórmula sumar fila hoja + sumar fila hoja2 
