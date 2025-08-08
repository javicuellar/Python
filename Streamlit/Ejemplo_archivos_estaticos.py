'''
omo aprendió en los fundamentos de Streamlit, Streamlit ejecuta un servidor al que se conectan los clientes. Esto significa que los espectadores de tu aplicación no tienen acceso directo a los archivos que son locales para tu aplicación. La mayoría de las veces, esto no importa porque los comandos de Streamlt se encargan de eso por usted. Cuando uses, tu servidor Streamlit accederá al archivo y manejará el alojamiento necesario para que los espectadores de tu aplicación puedan verlo. Sin embargo, si desea una URL directa a una imagen o archivo, deberá alojarlo. Esto requiere establecer la configuración correcta y colocar los archivos alojados en un directorio denominado . Por ejemplo, su proyecto podría verse así:st.image(<path-to-image>)static

your-project/
├── static/
│   └── my_hosted-image.png
└── streamlit_app.py
Para obtener más información, lea nuestra guía sobre el servicio de archivos estáticos.
'''
'''
Ejemplo de uso

  - Poner una imagen en la carpeta cat.png./static/
  - Añade under en tu enableStaticServing = true[server].streamlit/config.toml
  - Cualquier medio de la carpeta se sirve en la URL relativa como ./static/app/static/cat.png
'''

# .streamlit/config.toml

[server]
enableStaticServing = true


# app.py
import streamlit as st

with st.echo():
    st.title("CAT")

    st.markdown("[![Click me](app/static/cat.png)](https://streamlit.io)")

