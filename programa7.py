#Escribe una función que calcule la mediana de una lista de números. Usa la función sort de list para ordenar la lista. 
def mediana(lista):
    lista.sort
    n= len(lista)
    if n % 2 == 1:
        return lista[n//2]
    else:
        x1= lista[n//2-1]
        x2=lista[n//2]
        return(x1+x2)/2
x=int(input("ingrese el numero de numeros "))
lista=[]
for i in range (x):
    y=int(input(f"ingrese numero {i+1} "))
    lista.append(y)
med=mediana(lista)
print(f"la mediana es de {med}")