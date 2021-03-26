"En tal sentido, te solicitamos que escribas un programa en pseudocódigo que reciba cinco criptomonedas, cada una con sus"
"respectivas cantidades y precios en dólares americanos (USD), y luego imprima el valor total en USD que tienes acumulado"


i=0
valor=0.0
while i < 2:
      cripto = input("ingrese el nombre la moneda: ")
      cant = float(input("Ingrese la cantidad de la moneda: "))
      cotiz = float(input("Ingrese la cotización en USD de la moneda: "))
      valor = valor + (cant*cotiz)
      i+=1

print("Usted tiene "+str(valor)+" Dólares Americanos")

