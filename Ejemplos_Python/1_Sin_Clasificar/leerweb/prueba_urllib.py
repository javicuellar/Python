# M�dulo de lectura de webs
# --------------------------

import urllib.request as u

def LeerWeb1():
    response = u.urlopen('http://google.com')

    for line in response:
        print (line.rstrip())


#  No encuentra el m�dulo urllib2
# import urllib2

def LeerWeb2():
    r = u.urlopen ('http://www.python.org')
    print (r.read(200))		# lectura de los 100 primeros caracteres


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