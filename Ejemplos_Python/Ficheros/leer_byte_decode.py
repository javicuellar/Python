# -*- coding: utf-8 -*-

dic = {u"£": u'ú', u'¤': u'ñ', u'¢': u'ó', u'¡': u'í', u'‚': u'é' }


with open("fichero.tmp", "rb") as f:
	byte = f.read(1)
	while byte != b'':
		linea = u''
		while byte != b'\r':
			if byte == b'\x81':
				# caracter no transformado que da error
				byte = b'u'
			s = byte.decode(u'cp1252')
			if s in dic:
				s = dic[s]			
			linea += s
			byte = f.read(1)
		print (linea)
		byte = f.read(1)
		byte = f.read(1)
