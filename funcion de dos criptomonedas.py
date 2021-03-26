#compare las cotizaciones de dos criptomonedas e indique cuál es la más rentable,
#si tienen las misma rentabilidad que retorne la primera criptomoneda:


def MayorRentabilidad(cotiz1, cotiz2):

      if cotiz1 >= cotiz2:
            masRentable = "cotiz1";
      else :
            masRentable = "cotiz2";

      return masRentable
           
MayorRentabilidad(0, 1)
