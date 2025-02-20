#Escribe una función que implemente un juego de adivinanza donde el usuario debe adivinar un número 
#generado aleatoriamente por la computadora. La función debe proporcionar pistas sobre si el número ingresado es 
#mayor o menor que el número objetivo. 
import random
n=int(input("ingrese el numero maximo que puede estar "))
x= random.randint(1, n)
y=int(input("ingrese el numero que cree puede ser "))
while y != x:
    if y > x:
        print(" el numero que ingreso es mayor ")
    elif y < x:
        print(" el numero que ingreso es menor ")
    y=int(input("ingrese el numero que cree puede ser "))

print("el numero que ingreso es igual")
