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

from Herramientas.sheet import Actualizar_Hoja



def Alerta_viaje_esqui(terminos_busqueda):
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
        resultados_termino = []
        resultados = []
        while len(resultados) < 30:
            resultados = driver.find_elements(By.CSS_SELECTOR, "h2 a")

            try:
                caja_mas_resultados = driver.find_element(By.ID, "more-results")
                caja_mas_resultados.send_keys(Keys.RETURN)

                time.sleep(random.randint(2,5))
            except Exception:
                break

        for resultado in resultados:
            try:
                titulo = resultado.text                     # Texto del enlace (título del resultado)
                enlace = resultado.get_attribute("href")    # Enlace del resultado
                if titulo and enlace:
                    resultados_termino.append({
                        "Búsqueda": termino,
                        "Título": titulo,
                        "Enlace": enlace
                        })
            except Exception:
                continue

        resultados_globales.extend(resultados_termino)

    driver.quit()

    df = pd.DataFrame(resultados_globales)
    
    Actualizar_Hoja('Alertas Esqui', df)
    # df.to_excel("Alertas Esqui.xlsx", index=False)



if __name__ == "__main__":
    terminos = [
        "viaje esqui ayuntamiento",
        "viaje esqui ayuntamiento 2025",
        ]
    
    Alerta_viaje_esqui(terminos)

    print("Búsqueda finalizada. Resultados guardados en 'Alertas Esqui'")
