#FizzBuzz si un numero es divisible entre 3 se imprime Fizz, si es divisible  5 se imprime Buzz
# si es divisible en 3 y 5 se imprime FizzBuzz y sino se imprime el numero en cuestion

num= int(input("por favor ingrese un numero entero : "))


if num%3==0 and num%5==0:
      print("FizzBuzz")
elif num%3==0:
      print("Fizz")
elif num%5==0:
      print("Buzz")
else: print(num)
