import os
from dotenv import load_dotenv



load_dotenv('config.env')

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
path = os.getenv("FILEPATH")
secreto = os.getenv("SECRETO")

print("Usuario.- ", username)
print("Password.- ", password)
print("Path.- ", path)
print("Secreto.- ", secreto)