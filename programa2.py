#Escribe una función que reciba un número arbitrario de argumentos y devuelva su suma.
def suma(n):
    s=0
    for i in n:
        s=s+i
    return s
x=int(input("ingrese el numero de numeros que va ingresar "))
lista=[]
for j in range (x):
    y=int(input(f"ingrese el numero {j+1} " ))
    lista.append(y)
s=suma(lista)
print("la suma de todos los numero es de ", s)
    