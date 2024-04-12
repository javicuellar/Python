# Librerías Python para manejo de fotos


### Enlaces de interes consultados

- [Python - usar 4 líneas para combinar muchos ficheros CSV](https://twitter.com/TomMitchellData/status/1766523617280454702?t=j7LYIITv3wg-GIBdi-_xtw&s=03)
- [Reconocimiento facial con deep learning y python](https://cienciadedatos.net/documentos/py34-reconocimiento-facial-deeplearning-python)


### Pruebas pendientes de realizar y documentar

  - Probar librerías de reconocimiento facial, es rápido o muy lento? puedo usar?


#### Metadatos

* Exiftool - Librería para recuperar metadatos, NECESITA TENER INSTALADO EXIFTOOL.EXE
* pyexiv2 - Recupera metadatos, permite su modificación, etc.

  Hacemos pruebas con varias fotos para consultar sus metadatos.
  
  También probamos con fotos tratadas en NAS **Sygnology por aplicación Photos**. Queremos saber:
    - Fecha foto -> coge la fecha de modificación (ignora la de creación)
    
    - Las etiquetas -> se graban en:
      * read_raw_xmp() 
      * read_iptc().items() "Iptc.Application2.Keywords"
      * read_xmp().items()  "Xmp.dc.subject"  y en algunos casos  "Xmp.MicrosoftPhoto.LastKeywordXMP"
    
    - Donde y como se graba la información de reconocimeinto facial 
      * read_raw_xmp() tiene dos "etiquetas"
        - <?xpacket begin="" id="..."?>   -> "primera etiqueta"
        - xmpMM:InstanceID="uuid:....."   -> no está en todas
    
    * Probamos Si ponemos el metadato de reconocimiento facial en una foto sin la cara, la aplicación Photos la reconocerá? Es decir podemos marcar nosotros y pasar la info a Photos?  ->  NO FUNCIONA.
