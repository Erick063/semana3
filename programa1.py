# Escribe una función que reciba el nombre y la edad de una persona, y muestre un mensaje. Si la edad no 
# se proporciona, debe asumir que es 18. 
def men(nom, edad = 18):
    print(f"su nombre es {nom} y  su edad es {edad}")
    return
nom = input(" ingrese su nombre ")
edad = int(input("ingrese su edad "))
men(nom, edad)