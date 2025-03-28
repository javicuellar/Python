import load as cg
import pokemon as pk
from PIL import Image

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

def main():
    """
    Función principal para buscar y mostrar información sobre un Pokémon.
    Carga una lista de Pokémon desde un archivo CSV, solicita al usuario un nombre de Pokémon para buscar,
    y muestra la información del Pokémon encontrado, incluyendo su nombre, tipos y la imagen asociada si existe.
    """

    # Cargar la lista de Pokémon desde un archivo CSV
    pokemon_list = cg.load_file("poke_db\\pokemon.csv")    

    # Solicitar al usuario el nombre del Pokémon a buscar
    pokemon_name = input("Pokemon Search >> ")    

    # Buscar el Pokémon en la lista cargada
    pokemon = search_pokemon(pokemon_list, pokemon_name.lower())
    
    # Si se encuentra el Pokémon, mostrar su información y la imagen asociada
    if pokemon != None:
        print(pokemon.get_name().capitalize(), pokemon.get_type1(), pokemon.get_type2())    
        img = Image.open("poke_db\\" + pokemon.get_img())
        img.show()

main()