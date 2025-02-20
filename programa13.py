#Escribe una función que determine si un año dado es bisiesto o no.
def bis(n):
    if (n % 400 == 0) or (x % 4 == 0 and x % 100 != 0 ):
        print(" si es un año bisiesto")
    else:
        print(" no es un año bisiesto")
x=int(input("ingrese un año "))
bis(x)