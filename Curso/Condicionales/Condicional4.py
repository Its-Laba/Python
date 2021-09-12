'''
    Condicional4.py
    Escribir un programa que pregunte al usuario su renta anual y muestre
    por pantalla el tipo impositivo que le corresponde.
'''

renta = int(input("Introduzca su renta:  "))

if(renta < 10000):
    print("Tipo impositivo : 5%")
elif(10000 <= renta < 20000):
    print("Tipo impositivo : 15%")
elif(20000 <= renta < 35000):
    print("Tipo impositivo : 20%")
elif(35000 <= renta <= 60000):
    print("Tipo impositivo : 30%")
else:
    print("Tipo impositivo : 45%")
