 #te solicitamos escribir un programa en pseudocódigo que reciba cinco criptomonedas,
 #cada una con sus respectivas cantidades y precios en dólares americanos (USD), y luego
 #imprima el valor total en USD que tienes. La captura de los datos se debería poder utilizar
 #en diferentes partes de un pseudocódigo más complejo.

def capturar_moneda():

      cripto = input("ingrese el nombre la moneda: ")
      cant = float(input("Ingrese la cantidad de la moneda: "))
      cotiz = float(input("Ingrese la cotización en USD de la  moneda: "))
      return cant * cotiz

valor=0.0
i=0
while i < 3 :
       valor = valor + capturar_moneda()
       i+=1

print("Usted tiene "+str(valor)+" Dólares Americanos")
