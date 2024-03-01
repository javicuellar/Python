from bs4 import BeautifulSoup
import requests

def LeerWeb3():
    # url = input('Escribe web: ')

    r = requests.get ('http://www.infomercados.com/cotizaciones/historico/bbva-bbva/')

    data = r.text
    soup = BeautifulSoup(data, "html.parser")		# analiza, scraping

    for link in soup.find_all('a'):
        print(link.get('href'))

LeerWeb3()