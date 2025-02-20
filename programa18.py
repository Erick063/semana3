#Escribe una función que calcule la mediana de una lista de números. 
def calcular_mediana(lista):
    lista_ordenada=sorted(lista)
    n=len(lista_ordenada)
    if n % 2 == 0:
        n1=lista_ordenada[n//2-1]
        n2=lista_ordenada[n//2]
        mediana = (n1+n2)/2
    else:
        mediana= lista_ordenada[n//2]
    return mediana
numeros= [4, 2, 9, 1, 5, 6]
resultado = calcular_mediana(numeros)
print("la mediana es:", resultado)