# Escribe una función que calcule el determinante de una matriz 3x3.
def matriz(lista1, lista2, lista3):
    a, b, c=lista1
    d, e, f=lista2
    g, h, i=lista3
    s=(a*e*i)+(d*h*c)+(g*b*f)
    r=(c*e*g)+(f*h*a)+(i*b*d)
    det=s-r
    return det
lista1=[]
lista2=[]
lista3=[]
for i in range(3):
    for j in range(3):
        x=int(input(f"ingrese el numero de fila {i+1} y columna {j+1} "))
        if i == 0:
            lista1.append(x)
        elif i==1:
            lista2.append(x)
        elif i==2:
            lista3.append(x)

det=matriz(lista1, lista2, lista3)
print(det)
