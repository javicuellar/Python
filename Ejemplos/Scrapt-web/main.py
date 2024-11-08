from Common import tools



#  No consiguo que funcione, se produce el error 403

url = "https://es.investing.com/equities/spain"


# html = tools.getUrl(url)
# html = tools.LeerWeb(url)
html = tools.socketUrl(url)