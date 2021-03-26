#Supongamos que dado un valor n queremos calcular
#el valor de su factorial (n!). Luego, utilizando un ciclo for tendríamos el siguiente programa:

n = int(input("Valor a calcular el factorial: "))
fact = 1
for elem in range(1,n+1):
      fact = elem * fact
print("El factorial de",n,"es",fact)
