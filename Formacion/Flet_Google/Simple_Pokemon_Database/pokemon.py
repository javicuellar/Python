class Pokemon:
    """
    Representa un Pokémon con atributos como nombre, tipos y una imagen.

    Attributes:
    - name (str): El nombre del Pokémon.
    - type1 (str): El primer tipo del Pokémon.
    - type2 (str): El segundo tipo del Pokémon.
    - img (str): La ruta o nombre de archivo de la imagen del Pokémon.
    """

    def __init__(self, name, pokemon_type1, pokemon_type2, img):
        """
        Inicializa un objeto Pokémon con nombre, tipos y una imagen.

        Args:
        - name (str): El nombre del Pokémon.
        - pokemon_type1 (str): El primer tipo del Pokémon.
        - pokemon_type2 (str): El segundo tipo del Pokémon.
        - img (str): La ruta o nombre de archivo de la imagen del Pokémon.
        """
        self.name = name
        self.type1 = pokemon_type1
        self.type2 = pokemon_type2
        self.img = img

    def set_name(self, name):
        """
        Establece el nombre del Pokémon.

        Args:
        - name (str): El nuevo nombre del Pokémon.
        """
        self.name = name

    def get_name(self) -> str:
        """
        Obtiene el nombre del Pokémon.

        Returns:
        - str: El nombre actual del Pokémon.
        """
        return self.name

    def set_type1(self, pokemon_type):
        """
        Establece el primer tipo del Pokémon.

        Args:
        - pokemon_type (str): El nuevo primer tipo del Pokémon.
        """
        self.type1 = pokemon_type

    def get_type1(self) -> str:
        """
        Obtiene el primer tipo del Pokémon.

        Returns:
        - str: El primer tipo actual del Pokémon.
        """
        return self.type1

    def set_type2(self, pokemon_type):
        """
        Establece el segundo tipo del Pokémon.

        Args:
        - pokemon_type (str): El nuevo segundo tipo del Pokémon.
        """
        self.type2 = pokemon_type

    def get_type2(self) -> str:
        """
        Obtiene el segundo tipo del Pokémon.

        Returns:
        - str: El segundo tipo actual del Pokémon.
        """
        return self.type2

    def set_img(self, img):
        """
        Establece la imagen del Pokémon.

        Args:
        - img (str): La nueva ruta o nombre de archivo de la imagen del Pokémon.
        """
        self.img = img

    def get_img(self) -> str:
        """
        Obtiene la imagen del Pokémon.

        Returns:
        - str: La ruta o nombre de archivo actual de la imagen del Pokémon.
        """
        return self.img
