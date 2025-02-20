def gcd(x,y):
    while y:
        x, y = y, x % y
    return x
def calcular_mcm(a,b):
    return (a*b//gcd(a,b))
numero1=int(input("Ingresa un numero: "))
numero2=int(input("Ingresa un numero: "))
mcm_resultante= calcular_mcm(numero1,numero2)
print(f"El MCM de {numero1} y {numero2} es de {mcm_resultante}")
#¿Cuál es el propósito de la función 'gcd' en el código proporcionado? 
#D. Calcular el máximo común divisor de dos números.

#En el cálculo del MCM, ¿qué papel juega el resultado de la función 'gcd'? 
#A. Se utiliza para dividir el producto de los números. 

#Si los números ingresados son 8 y 12, ¿cuál será el resultado de 'calcular_mcm'?
# C.24

#Si 'x' es inicialmente 15 y 'y' es 10 en la función 'gcd', 
#¿cuál será el primer valor de 'x' y 'y' en la primera iteración del bucle?
#B. x = 10, y = 5 


#Qué pasaría si se ingresara un número negativo en 'calcular_mcm'? 
#D. El MCM se calcularía como si el número fuera positivo.