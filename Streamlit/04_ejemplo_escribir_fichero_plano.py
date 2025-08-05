import streamlit as st

#### Grabar un fichero de texto
note = st.text_input('Enter a Note')

if note:
    with open('notes.txt', 'a+') as file:
        file.write(f'{note}\n')



####  Lectura del fichero
with open('notes.txt', 'r+') as file: 
    st.subheader('Lectura del fichero, notes.txt')
    st.text(file.read())
