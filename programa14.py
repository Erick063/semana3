def pol(n,x):
    res=0
    g=len(n)-1
    for i in range(len(n)):
        res+=n[i]*(x**(g-i))
    return res

x=int(input("ingrese el numero de coeficientes "))
lista=[]
for i in range (x):
    y=int(input(f"ingrese el coeficiente {i+1} "))
    lista.append(y)
z=int(input("ingrese el numero con el que se va evaluar "))
res=pol(lista, z)
print(f"el resultado es {res}")