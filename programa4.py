#Escribe una función que calcule la factorial de un número usando ciclos
def fact(n):
    mul=1
    for i in range(n,1,-1):
        mul=mul*i
        print(i, mul)
    return mul
x=int(input("ingrese el numero "))
y=fact(x)
print(y)