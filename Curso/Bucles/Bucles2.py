'''
    Bucles2.py
    Escribir un programa que pregunte al usuario una cantidad a invertir,
    el interés anual y el número de años, y muestre por pantalla
    el capital obtenido en la inversión cada año que dura la inversión.
'''

invertir = float(input("Introduzca la cantidad a invertir:  "))
interes = float(input("Introduzca el interes anual:  "))
years = int(input("Introduzca la cantidad de años:  "))
i = 0
while i < years:
    i += 1
    invertir *= 1 + interes / 100
    print(f"Capital obtenido en el año {i}:  {round(invertir,2)}")
