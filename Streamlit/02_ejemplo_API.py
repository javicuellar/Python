### Interacción con las API web
import requests

st.header('Guess Age From Name')
name = st.text_input('Your Name')

if name:
    r = requests.get(f'https://api.agify.io/?name={name}').json() 
    st.write(f'Your age is predicted to be {r["age"]}')



#### ejemplo de la API de Pokémon
import streamlit as st, requests

st.header('Pokemon Images')

mypokemon = ['charizard', 'pikachu', 'eevee', 'snorlax', 'garchomp', 'lucario']

pokemon = st.selectbox('Select a Pokemon', mypokemon)

if pokemon:
    r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
    for img in r['sprites'].values():
        if img is not None:
            if str(img)[-4:] == '.png':
                st.image(img)


### Ejemplo de API de base de datos de cócteles
import streamlit as st, requests

drinks = requests.get( f'https://thecocktaildb.com/api/json/v1/1/list.php?i=list').json()
ingredients=[]

for drink in drinks['drinks']:
    ingredients.append(drink['strIngredient1'])

##### THIS CODE RUNS IN THE BROWSER #####
st.title('The Cocktail DB API')
st.markdown('---')
selected = st.selectbox('Select an Ingredient', ingredients)
st.markdown('---')

if selected:
    st.header(f'Drinks with {selected}')
    
    ##### THIS CODE RUNS ON THE SERVER #####
    r = requests.get( f'https://thecocktaildb.com/api/json/v1/1/filter.php?i={selected}' ).json()
    for drink in r['drinks']:
        
        ##### THIS CODE RUNS IN THE BROWSER #####
        st.subheader(drink['strDrink'])
        st.image(drink['strDrinkThumb'])
