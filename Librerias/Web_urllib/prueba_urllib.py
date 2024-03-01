#   MOdulo de lectura de webs
# --------------------------
import urllib.request as u

def LeerWeb1():
    response = u.urlopen('https://www.google.com/')

    print(response.read(60))
    for line in response:
        print (line.rstrip())

LeerWeb1()

#   No encuentra el mÓdulo urllib2
# import urllib2

def LeerWeb2():
    r = u.urlopen ('http://www.python.org')
    print (r.read(200))		                    # lectura de los 200 primeros caracteres

LeerWeb2()