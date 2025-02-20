#Escribe una función que calcule el máximo común divisor (MCD) de dos números. 
def MCD(a,b):
    while b!=0:
        a, b = b, a%b
    return a
    
a=int(input("ingrese un numero "))
b=int(input("ingrese un numero "))
x= MCD(a,b)
print(f"el maximo comun divisor es {x}")