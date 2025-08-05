import streamlit as st
import pandas as pd


## https://docs.streamlit.io/library/api-reference/widgets

st.title('Title')
st.header('Header')
st.subheader('Subheader')
st.caption('Caption')
st.code('print("this is some code")')
st.text('Text')
st.markdown('- *Markdown*')
st.latex('\sum_{k=0}^{n-1} ar^k')

st.dataframe(pd.DataFrame({'a':[1, 2, 3],'b':['A', 'B', 'C']}))
st.table({'a':[1, 2, 3],'b':['A', 'B', 'C']})

st.metric('Temp', '75', '5')
st.metric('Wind', '9', '-4')

st.json({'a':[1, 2, 3],'b':['A', 'B', 'C']})

st.button('Button')
st.download_button('Download Button', b'asdf')

st.checkbox('Checkbox')
st.radio('Radio',[1,2,3])
st.selectbox('Selectbox', ['a','b','c'])
st.multiselect('Multiselect', ['a','b','c'])

st.slider('Slider')
st.select_slider('Select Slider', ['a','b','c'])

st.text_input('Text Input')
st.number_input('Number Input')
st.text_area('Text Area')
st.date_input('Date Input')
st.time_input('Time Input')

st.file_uploader('File Uploader')

st.camera_input('Camera')
st.color_picker('Color Picker')

st.image('tulips.jpg')
st.audio('audio.mp3')
st.video('video.mp4')

### Menú lateral
st.sidebar.selectbox('Menu', ['a','b','c'])

### Columnas
col1, col2 = st.columns([1,2])
col1.text_input('Thinner Column')
col2.text_input('Thicker Column')

### Pestañas
tab1, tab2 = st.tabs(['TAB 1','TAB 2'])
tab1.text_area('text in tab 1')
tab2.date_input('date in tab 2')

st.expander('Expander')
st.container()

placeholder = st.empty()
placeholder.text('Hide this placeholder container')

if st.button('Hide'): 
    placeholder.empty()
    
### Progreso y animaciones
st.progress(35)

### ????
st.spinner('Spinner')

if st.checkbox('Balloons', False): 
    st.balloons()
if st.checkbox('Snow', False): 
    st.snow()

st.error('Error')
st.warning('Warning')
st.info('Info')
st.success('Success')

st.exception(RuntimeError('This is a fake error.'))

# st.form('')
# # st.form_submit_button('')import numpy as np

import numpy as np
df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)


treemap = pd.read_csv('trees2.csv')
st.write(treemap)
st.map(treemap)
