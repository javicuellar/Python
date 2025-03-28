from selenium import webdriver

# Configurar el WebDriver (usando Chrome en este ejemplo) 
driver = webdriver.Chrome() 

# Navegar a la página web deseada 
driver.get('https://www.example.com') 

# Obtener el código fuente HTML de la página 
html_source = driver.page_source 

# Imprimir el código fuente HTML 
print(html_source) 

f = open("web.html", "w")
f.write(html_source)
f.close()

# Cerrar el WebDriver 
driver.quit()
