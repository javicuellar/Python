import os

class Fichero(object):
    def __init__(self, r, n, e):
        self.ruta = r
        self.nombre = n
        self.extension = e
    def nombre_completo(self):
	    return str(self.ruta + os.sep + self.nombre + self.extension)

class Directorio(Fichero):
    def __init__(self,r):
        self.ruta = r
        self.nombre = ''
        self.extension = ''
        lis = []
        for (ru,d,a) in os.walk(r):
            for ar in a:
                (n,e) = os.path.splitext(ar)
                f = Fichero(r,n,e)
                lis.append(f)
        self.ficheros = lis

    def nombre_completo(self):
	    return str(self.ruta)
    
    def listar_ficheros(self):
        print ('Ruta: ' + self.ruta)
        for f in self.ficheros:
	        print ('  --> ', f.nombre_completo())


d = Directorio(os.getcwd())
print (d.nombre_completo())
print (d.listar_ficheros())
