from datetime import datetime

nombreCripto=input("Nombre de la Criptomoneda: ")
cantCripto=float(input("Cantidad acumulada de la Criptomoneda: "))
cotizacion=float(input("Cotización por US$ del día de la Criptomoneda: "))

hora = datetime.now()
hora=hora.strftime("%d/%m/%y %I:%M:%S %p")

print("La fecha completa y hora en la que obtuvo la información fue:"+str(hora))

valorTotal= cantCripto * cotizacion
Tasa=1.05

print("Ud. Posee un total de US$ "+str(valorTotal))
valorTotal1=valorTotal  *Tasa
valorTotal2=valorTotal1*Tasa
valorTotal3=valorTotal2*Tasa
valorTotal4=valorTotal3*Tasa
valorTotal5=valorTotal4*Tasa
valorTotal6=valorTotal5*Tasa
valorTotal7=valorTotal6*Tasa
ganancia= valorTotal7-valorTotal

print("Su ganancia luego de una semana es: "+str(ganancia)+"USD")
