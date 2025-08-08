'''
Por supuesto, es posible que se pregunte dónde van su nombre de usuario y contraseña. Streamlit tiene un mecanismo conveniente para la administración de secretos. Por ahora, veamos cómo funciona muy bien con los secretos. En el directorio local del proyecto, puede guardar un archivo. ¡Guardas tus secretos en el archivo toml y simplemente los usas! Por ejemplo, si tienes un archivo de aplicación, el directorio del proyecto puede tener el siguiente

your-LOCAL-repository/
├── .streamlit/
│   └── secrets.toml # Make sure to gitignore this!
└── streamlit_app.py


Para el ejemplo SQL anterior, su archivo podría verse de la siguiente manera:secrets.toml

[connections.my_database]
    type="sql"
    dialect="mysql"
    username="xxx"
    password="xxx"
    host="example.com" # IP or URL
    port=3306 # Port number
    database="mydb" # Database name
'''

