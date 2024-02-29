from SQLite import createtabla as C
from SQLite import insert as I
from SQLite import select as S

def ejemplos():
    #print (C.creatabla())
    #print (I.insertaregistro())
    #print (I.insertavalores('Javi','Guapo',47))
    #valores=['Clara','Reina',39]
    #print(I.insertatupla(valores))
    #print(S.selecttodo())

    edad=10
    print(S.selectmutiplevar(edad))

ejemplos()