from sql_comandos import createtabla as C

from sql_comandos import insert as I
from sql_comandos import select as S


print (C.creatabla())

print (I.insertaregistro())

print (I.insertavalores('Javi','Guapo',47))

valores=['Clara','Reina',39]

print(I.insertatupla(valores))

print(S.selecttodo())

edad= 10
print(S.selectmutiplevar(edad))