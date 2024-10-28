import sys
import os
from github import Github
from dotenv import load_dotenv



load_dotenv('config.env')

username = os.getenv("GITUSER")
password = os.getenv("GITPASSWORD")
path = os.getenv("FILEPATH")

print('Usuario: ', username)
print('Password: ', password)
print('Carpeta: ', path)


def create():
    folderName = str(sys.argv[1])
    folderpath = os.path.join(path, folderName)
    if os.path.exists(folderpath):
        print("La carpeta existe.. " + folderpath)
    os.makedirs(folderpath)
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Se ha creado satisfactoriamente el repositorio {}".format(sys.argv[1]))


if __name__ == "__main__":
    create()