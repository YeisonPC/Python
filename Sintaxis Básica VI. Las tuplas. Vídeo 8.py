#las tuplas son mas rapidas que us String pero las tuplas no se puedesn editar
#una tupla va con () y una lista con[]
mitupla=("Yeison",1,7,1991)#creamos una tupla
print(mitupla[2])

#se puede convertir una tupla en lista y listas en tuplas
milista=list(mitupla)#tupla a lista
print(milista)
#lista a tupla
mitupla2=tuple(milista)
print(mitupla2)
#contar los elementos especificos en una tupla
print(mitupla.count(7))
#longitud de la tupla
print(len(mitupla))

#tupla unitaria
mitupla3=("Yeison",)
print(len(mitupla3))

#las tuplas se puede escribir sin () o empaquetado de tupla
mitupla4="Yeison",1,7,1991#creamos una tupla
print(mitupla4)
nombre, dia, mes, anio=mitupla4#desempaquetado de tupla
print(nombre)
print(dia)
print(mes)
print(anio)