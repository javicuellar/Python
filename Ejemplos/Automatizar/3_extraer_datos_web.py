import requests
from bs4 import BeautifulSoup



url = 'https://news.ycombinator.com/'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')


for item in soup.find_all('tr', class_='athing submission'):
    print(item.text)

