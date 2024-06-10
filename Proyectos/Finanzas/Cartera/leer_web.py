import requests
import bs4
from bs4 import BeautifulSoup
import re
import funciones as f


def LeerPrecio(tipo, activo, ticket):
    if tipo == 'FONDO' or tipo == 'ETF':
        if tipo == 'FONDO':
            urlFondo = "https://www.morningstar.es/es/funds/snapshot/snapshot.aspx?id="
            url = urlFondo + ticket
        else:
            url1 = "https://www.morningstar.es/es/etf/snapshot/snapshot.aspx?id="
            url2 = "&InvestmentType=FE"
            ticket = "0P0000YXKB"
            url = url1 + ticket + url2

        html = requests.get(url)
        soup = BeautifulSoup(html.text, "lxml")

        try:
            precio = str(soup.find(class_="line text"))
            precio = precio[precio.find('>') + 1:]
            valor = f.ExtraerNum(precio[:precio.find('<')])
        except:
            print(url)
            print(" > Línea precio: ", precio)
            print(" -> Error extraer precio MorningStar: ", ticket, " Activo: ", activo)
            valor = 0    
    
    elif tipo == 'ACCIÓN':
        url1 = "https://tools.morningstar.es/es/stockreport/default.aspx?Site=es&id="
        url2 = "&LanguageId=es-ES&SecurityToken="
        url3 = "]3]0]E0WWE$$ALL"
        url = url1 + ticket + url2 + ticket + url3

        html = requests.get(url)
        soup = BeautifulSoup(html.text, "lxml")

        try:
            for l in soup.find(class_="price"):
                valor = f.ExtraerNum(l)
        except:
            print(" -> Error extraer precio MorningStar: ", ticket, " Activo: ", activo)
            valor = 0

    elif tipo == 'P.PENSIÓN':
        url1 = "https://tools.morningstar.es/2nhcdckzon/snapshot/snapshot.aspx?SecurityToken="
        url2 = "]2]0]FOESP$$PEN"
        url = url1 + ticket + url2
        
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "lxml")

        try:
            cont = 0
            for l in soup.find_all(class_="value_div text-right text"):
                cont += 1
                if cont == 4:
                    precio = [float(s) for s in re.findall(r'-?\d+\.?\d*', str(l))]
                    valor = precio[0]
                    break
        except:
            print(" -> Error extraer precio MorningStar: ", ticket, " Activo: ", activo)
            valor = 0

    else:
        valor = 1
    return valor
