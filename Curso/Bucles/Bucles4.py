'''
    Bucles4.py
    Escribir un programa que muestre el eco de todo lo que
    el usuario introduzca hasta que el usuario escriba “salir” que terminará.
'''
import time

print("Comencemos el juego.\nA continuación va a jugar con la maquina como \
si esta fuera un niño pequeño repetirá todo hasta que inserte: \"salir\"")
input("Pulse enter para iniciar.")
time.sleep(1)
clave = input()
while(clave.lower() != "salir" ):
    print(clave)
    clave = input()
print("Juego terminado!!\nGracias por Jugar :)")
