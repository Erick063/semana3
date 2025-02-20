#Escribe una función que determine si una cadena de texto es un palíndromo
tx=input("ingrese un texto ")
y= tx[::-1]
if y==tx:
    print("el texto es palindromo")
else:
    print("no es palindromo")