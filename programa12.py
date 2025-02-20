#Escribe una función que calcule la moda de una lista de números. 
def moda(lista):
    may=0
    moda=[]
    for i in range(len(lista)):
        cont=0
        for j in range(len(lista)):
            if lista[i]==lista[j]:
                cont+=1
        if cont > may:
            moda=[lista[i]]
        elif cont == may and lista[i] not in moda: 
            moda.append(lista[i])
    return moda
x=int(input("ingrese el numero de numeros "))
lista=[]
for i in range (x):
    y=int(input(f"ingrese el numero {i+1} "))
    lista.append(y)
moda = moda(lista)
print("la moda es ", moda)
