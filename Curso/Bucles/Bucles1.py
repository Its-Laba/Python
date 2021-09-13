'''
    Bucles1.py
    Escribir un programa que pida al usuario un número entero positivo y
    muestre por pantalla todos los números impares desde 1
    hasta ese número separados por comas.
'''

num = int(input("Introduce un numero:  "))
i = 1
print(f"Los numeros impares hasta {num} son: ",end = " ")
while i < num:
    print(f"{i} ",end = " ")
    i += 2
