import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de InfoJobs para buscar trabajos de informática
url = "https://www.infojobs.net/ofertas-trabajo?keyword=informatica&provinceIds=33&segmentId=&page=1&sortBy=RELEVANCE&onlyForeignCountry=false&countryIds=17&sinceDate=ANY"

# Realiza la solicitud GET a la página
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar los contenedores de trabajos
    job_cards = soup.find_all('div', class_='offer-details')

    # Listas para almacenar los datos
    titles = []
    companies = []
    locations = []
    dates = []

    # Recorrer las tarjetas de trabajo y recoger información
    for job in job_cards:
        title = job.find('a', class_='offer-title').text.strip()
        company = job.find('span', class_='offer-company').text.strip()
        location = job.find('span', class_='offer-location').text.strip()
        date = job.find('span', class_='offer-date').text.strip()

        titles.append(title)
        companies.append(company)
        locations.append(location)
        dates.append(date)

    # Crear un DataFrame con los datos recogidos
    df_jobs = pd.DataFrame({
        'Título': titles,
        'Empresa': companies,
        'Ubicación': locations,
        'Fecha': dates
    })

    # Mostrar el DataFrame
    print(df_jobs)
else:
    print(f"Error al acceder a la página: {response.status_code}")