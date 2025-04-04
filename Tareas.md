# Tareas
========

### Otras
----------

* FOTOS NAS.- Archivar.

* Incluir en los backups directorio Python_NAS


### Python

* Alertas.- En alerta_ficheros, analizar como incluir el tamaño de ficheros como parámetro. Y poner fuera del contenedor, en el volumen, para poder modificar automáticamente.
    Poner Alertas como un demonio que se ejecuta cada 5 minutos.
    - Incluir alerta de ficheros, duplicados.

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
