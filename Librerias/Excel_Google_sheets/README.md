APIs acceso a Google Sheets

  - gspread.- Funciona  (https://docs.gspread.org/en/latest/user-guide.html)
  - pygsheets.- No logré que funcionará bien, parte si me funciona. 



CREAR CREDENCIALES EN GOOGLE CLOUD PLATFORM - https://console.cloud.google.com/

    1) Crear proyecto
    2) Habilitar APIs => Biblioteca de API -> Google Drive API y Google Sheets API (HABILITAR)
    3) Crear credenciales (desde pantalla de API, arriba derecha)
        - API que usamos -> Google Drive API
        - Acceso -> Datos de aplicación
        - Uso Computer Engine, ... -> No
    4) Crear Cuenta de Servicio
        - Nombre.- rellenar con tu nombre o AppServicio, ...
        - Rol para la cuenta -> Proyecto -> Editor
        - Usuarios (opcional) -> "nada"
    5) Credenciales (panel izquierdo "APIs y Servicio" -> Credenciales)
        - Vemos que ya tenemos la cuenta de servicio, pulsamos sobre el correo (mail)
        - En pestaña CLAVES -> Agregar claves -> descargar json

      Una vez completado, tenemos el correo de la cuenta de servivio y el fichero json que hay que
    dejar en la carpeta donde esté nuestro programa Python.


IMPORTANTE
----------

    * Las hojas que se manejan se crean con la cuenta(mail) de la aplicación, NO con la personal.
    * SE TIENE QUE COMPARTIR con nuestra cuenta gmail para verlo.


Ejemplos.-

    - https://github.com/ifrankandrade/api/tree/main/google-sheets