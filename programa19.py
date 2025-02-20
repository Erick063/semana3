import random
def generar_numero_aleatorios(n):
    lista=list()
    for i in range(n):
        lista.append(random.randint(1,100))
    return lista

resultado = generar_numero_aleatorios(10)
print("Numeros aleatorios:", resultado)

#¿Cuál es el propósito de la función generar_numeros_aleatorios(n)? 
#C. Crear una lista de números aleatorios de longitud n. 

#¿Cuál de las siguientes afirmaciones es verdadera sobre el 
#uso de random.randint(1, 100)` dentro de la función? 
#A. Es posible que genere números repetidos en la lista. 

#¿Qué tipo de dato retorna la función generar_numeros_aleatorios(n)?
#C. Una lista de números enteros.

#si se llama a `generar_numeros_aleatorios(0), ¿qué resultado se obtiene? 
#A. Una lista vacía. 

#¿Qué se imprime en la consola si se ejecuta `print('Números aleatorios:', resultado)` después de llamar a 
#`generar_numeros_aleatorios(10)`?
#C. Números aleatorios entre 1 y 100. 
