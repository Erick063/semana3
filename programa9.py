#Escribe una función que encuentre el segundo número mayor en una lista de números. 
def sm(lista):
    lista.sort()
    x=lista[-2]
    return x

x=int(input("ingrese el numero de numeros "))
lista=[]
for i in range (x):
    y=int(input(f"ingrese numero {i+1} "))
    lista.append(y)
sm=sm(lista)
print(f"el segundo numero mayor es {sm}")