import urllib.request

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}

def getUrl2(url):
    req = urllib.request.Request(url)
    print('>> Request')
    with urllib.request.urlopen(req, headers).decode('Utf-8') as response:
        print('>>>Urlopen')
        data = response.read()
        print('>>>>DAta -> ', data)
    return data


import requests

def getUrl(url):
    response = requests.get(url, headers=headers)

    if response.status_code == 403:
        print("Forbidden error occurred. Check server-specific issues or rate limiting.")


import urllib.request as u

def LeerWeb(url):
    response = u.urlopen(url, headers)

    print(response.read(1).text)
    for line in response:
        print (line.rstrip())


import socket

def socketUrl(url):
    misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    misock.connect((url, 80))
    misock.send(b'GET '&url&' HTTP/1.0\n\n')

    while True:
        datos = misock.recv(512)
        if ( len(datos) < 1 ):
            break
        print (datos)

    misock.close()