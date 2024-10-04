import flet as ft
import load as cg
import pokemon as pk

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



def search_pokemon(pokemons: dict, name: str) -> pk.Pokemon:
    """
    Busca un Pokémon por su nombre en un diccionario de Pokémon.

    Args:
    - pokemons (dict): Un diccionario que contiene los datos de los Pokémon, donde las claves son los nombres de los Pokémon.
    - name (str): El nombre del Pokémon que se desea buscar.

    Returns:
    - pk.Pokemon or None: Si se encuentra el Pokémon, devuelve un objeto pk.Pokemon con los datos correspondientes.
                          Si no se encuentra, devuelve None.
    """
    pokemon = pokemons.get(name)

    if pokemon != None:        
        pokemon = pk.Pokemon(name, pokemon["Type1"], pokemon["Type2"], "poke_db\\images\\" + name + ".png")  
        return pokemon
    
    return None

def main(page: ft.Page):
    page.window.width = 320
    page.window.height = 320
    page.window.resizable = False
    page.padding = 24
    page.margin = 24

    pokemon_list = cg.load_file("poke_db\\pokemon.csv")    

    pokemon_name = ft.TextField(label="Pokemon name", autofocus = True)
    greetings = ft.Column()
    image = ft.Image(src = "poke_db\\images\\empty.png")

    def btn_click(e):      
        pokemon = search_pokemon(pokemon_list, pokemon_name.value.lower())
        if search_pokemon(pokemon_list, pokemon_name.value.lower()) != None:                    
            greetings.controls.clear()
            greetings.controls.append(ft.Text(f"Hello, {pokemon.get_name().capitalize()}!\nType: {pokemon.get_type1()}"))        
            image.src = pokemon.get_img()
        
        pokemon_name.value = ""        
        page.update()
        pokemon_name.focus()

    page.add(
        pokemon_name,
        ft.ElevatedButton("Pokemon Search", on_click = btn_click),
        greetings,
        image,        
    )

ft.app(
    target = main,
    assets_dir = "poke_db"
)