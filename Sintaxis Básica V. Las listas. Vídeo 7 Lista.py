milista=["Maria","Juan","Pepe","Karla","Sebastian"]
print(milista[:])#trae toda la lista
print(milista[2])#trae un dato en la posicion indicada
print(milista[0:3])#tra solo los primero tres elementos
print(milista[:4])#forma abrebiada del print de arriba
print(milista[2:])#trae los ultimos registros a partir de la posicion 2

milista.append("Sandra")#Agrega el registro en la ultima posicion
print(milista[:])

milista.insert(2,"Kamilo")#agrega el registro en la posicion 2
print(milista[:])

milista.extend(["Pablo","Luis","Yeison"])#añade varios registro
print(milista[:])

print(milista.index("Karla"))#trae la posicion del registro

print("Pepe" in milista)#indica si el registro existe o no

milista2=["Maria",True,6,False,8,"Maty"]# la lista puede contener varios tipos de variables
print(milista2[:])

milista2.remove("Maria")#elimina el registro indicado
print(milista2[:])

milista2.pop()#elimina el ultimo registro de la lista
print(milista2[:])

milista3=milista+milista2# suma las dos listas
print(milista3[:])

milista4=(["Paco","MAty","Jeus"]*3)#repite el vector las veces que se le indique
print(milista4[:])
