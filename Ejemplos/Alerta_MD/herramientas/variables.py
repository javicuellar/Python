import os
from dotenv import load_dotenv



class Variables():
    def __init__(self) -> None:
        load_dotenv('config.env')

        self.url = os.getenv("URL_MD")
        self.usuario = os.getenv("USER_MAIL")
        self.password = os.getenv("PASSWORD_MAIL")
        self.destinatario = os.getenv("DESTINATARIO")