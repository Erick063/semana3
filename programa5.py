#Escribe una función que reciba una lista de calificaciones y devuelva el promedio.
def pro(n):
    sum=0
    for j in n:
        sum= sum+j
    p=sum/len(n)
    return p
  
lista=[]
x=int(input("ingrese el numero de claificacion "))
for i in range (x):
    y=int(input(f"ingrese la calificacion {i+1} "))
    lista.append(y)
prom= pro(lista)
print(f"el promedio es de {prom}")