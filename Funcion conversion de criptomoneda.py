#ConversionCriptomoneda (…) que permite convertir una cantidad de dinero dada en bitcoins
#y ripples a dólares americanos; retornando el monto total resultante de la suma de los dosvalores
#calculados en dólares americanos. Estas son las equivalencias aproximadas:
#1 bitcoin = 7,442.50 USD$
#1 ripple=0.660982 USD$

def ConversionCriptomoneda( bitcoins, ripples:float): 
      bit=bitcoins*7442.50
      rip=ripples*0.660982
      total=bit+rip
      print(f"la cantidad de dólares americanos son : "+str(total))
      return 
      
