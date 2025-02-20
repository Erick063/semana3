#Escribe una función que reciba una cadena de texto y la devuelva invertida. 
def rev(tx):
    txt=tx[::-1]
    return txt
tx=input("ingrese un texto ")
txt = rev(tx)
print(f" el texto invertido es: {txt}")