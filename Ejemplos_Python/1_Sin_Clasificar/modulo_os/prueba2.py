import os
from datetime import datetime

formato = '%Y-%m-%d %H:%M:%S'  # establece formato de fecha-hora
tipos = {'.py':'Python', '.txt':'texto', '.jpg':'foto', '.mp4':'video', '.doc':'documento','.docx':'documento',
		'.xls':'excel', '.xlsx':'excel', '.ppt':'presentación', '.pptx':'presentación', '.pdf':'pdf',
		'.exe':'ejecutable'} 
sintipo = []

class Fichero(object):
    def __init__(self,r,a):
        self.ruta = r
        (self.nombre,self.extension) = os.path.splitext(a)
        self.nombre_completo = os.path.join(r, a)
        e = os.stat(self.nombre_completo)
        self.tamanio = int(round(e.st_size/1024))
        fec = datetime.fromtimestamp(e.st_ctime)
        self.fecha = fec.strftime(formato)
        self.tipo = ' '
        if self.extension in tipos:
            self.tipo = tipos[self.extension]
        elif not self.extension in sintipo:
            sintipo.append(self.extension)

class Directorio(Fichero):
	def __init__(self,r):
		self.ruta = r
		self.nombre = ''
		self.extension = ''
		self.nombre_completo = r
		l,dl,a,d =[],[],[],[]
		for (ru,d,a) in os.walk(r):
			break
		for ar in a:
			f = Fichero(ru,ar)
			l.append(f)
		self.ficheros = l
		for dr in d:
			sd = Directorio(os.path.join(ru, dr))
			dl.append(sd)
		self.subdirectorios = dl

	def listar_ficheros(self):
		if len(self.ficheros) != 0:
			for f in self.ficheros:
				print ('   --> ', f.nombre_completo, '    ', f.fecha, '     ', f.tamanio, 'Kb.')

	def listar_subdirectorios(self):
		print ('++> ', self.ruta)
		self.listar_ficheros()
		if len(self.subdirectorios) != 0:
			for dr in self.subdirectorios:
				dr.listar_subdirectorios()

	def contar_tipos_ficheros(self):
		d = {}
		for f in self.ficheros:
		    if f.tipo in d:
		        d[f.tipo] += 1
		    else:
		        d[f.tipo] = 1
		return d

	def contar_tipos(self):
		d = self.contar_tipos_ficheros()
		for f in self.subdirectorios:
			d.update(f.contar_tipos_ficheros())
		return d
		

path1 = os.getcwd()
path2 = '/home'

di = Directorio(path2)
#di.listar_ficheros()
di.listar_subdirectorios()
print ()
print ('sin tipo:', sintipo)
print ('contar tipos: ', di.contar_tipos())
