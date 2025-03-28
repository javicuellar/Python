#  Extraido de youtube url: https://www.youtube.com/watch?v=M5h0UW9SDDI&list=PL7HAy5R0ehQUqWhWNm3DpGOSAZ1skAEsW&index=21
import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



def buscar_duckduckgo(terminos_busqueda):
    chrome_options = Options()
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebkit/537.36 (KHTML, like Gecko) "
                                "Chrome/91.0.4472.77 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    resultados_globales = []
    for termino in terminos_busqueda:
        time.sleep(random.randint(1,5))     # esperar entre 1 y 5 segundos, simular ser humano

        driver.get("https://duckduckgo.com")
        driver.maximize_window()

        # Encontrar termino en caja de búsqueda
        caja_busqueda = driver.find_element(By.NAME, "q")
        caja_busqueda.send_keys(termino)
        caja_busqueda.send_keys(Keys.RETURN)

        # Esperar a que se carguen los resultados
        time.sleep(random.randint(2,5))
        
        # Extraer títulos y enlaces de los resultados
        resultados = driver.find_elements(By.CSS_SELECTOR, "h2 a")
        for resultado in resultados:
            try:
                titulo = resultado.text                     # Texto del enlace (título del resultado)
                enlace = resultado.get_attribute("href")    # Enlace del resultado
                if titulo and enlace:
                    resultados_globales.append({
                        "Término": termino,
                        "Título": titulo,
                        "Enlace": enlace
                        })
            except Exception:
                continue
    
    driver.quit()

    return resultados_globales




if __name__ == "__main__":
    # Ejemplos de términos de búsqueda
    terminos = [
        "automatización con Python",
        "mejores prácticas en Selenium",
        "automatizar búsquedas en DuckDuckgo"
    ]
    resultados_obtenidos = buscar_duckduckgo(terminos)

    df = pd.DataFrame(resultados_obtenidos)
    print(df)

    df.to_excel("resultados_duckduckgo.xlsx", index=False)
    print("Búsqueda finalizada. Resultados guardados en 'resultados_duckduckgo.xlsx'")
