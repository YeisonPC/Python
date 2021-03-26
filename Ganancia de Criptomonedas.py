"Te proponemos escribir un programa en Python que nos permita calcular la ganancia de una criptomoneda (Nombre y Cantidad),"
"si ésta se negocia por una cantidad de días indicada por el usuario y a una ganancia fija indicada también por el usuario. Al terminar,"
"el programa debe indicar la ganancia en cantidad de criptomoneda, la cantidad de días negociados y el monto total al finalizar los días."

Nombre_Criptomoneda=input("Nombre de la CritoMoneda : ")
Cantidad_CM=int(input("Cantidad de CritoMoneda : "))
dias=int(input("Cantidas de dias a negociar : "))
Ganancia=float(input("Ganancia de las Criptomonedas por dias : "))

ganancias_totales=(     (Cantidad_CM*Ganancia)  /100) *dias
cantidad_total=Cantidad_CM+ganancias_totales

print("La ganancia de",Nombre_Criptomoneda,"durante los ",dias," dia(s) es",str(ganancias_totales))

print("El monto total de",Nombre_Criptomoneda,"a los",str(dias)," dia(s)es de",cantidad_total)
