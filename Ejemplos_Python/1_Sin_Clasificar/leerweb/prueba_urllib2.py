# M�dulo de lectura de webs
# --------------------------

import urllib.request as u
 
response = u.urlopen('http://google.com')
 
for line in response:
    print (line.rstrip())


#  No encuentra el m�dulo urllib2
# import urllib2
# r = urllib2.urlopen ('https//www.python.org')
# print (r.read(100))		# lectura de los 100 primeros caracteres
