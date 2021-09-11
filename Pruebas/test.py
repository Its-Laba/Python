# "Primer programa de prueba en Python y con Atom"

# Se trata de un programa que pide dos numeros para una Suma y escribe
# tantos nombres como el resultado de la Suma

num1 = int(input("Introduce el primer sumando: "))
num2 = int(input("Introduce el segundo sumando: "))
sum = num1 + num2

if (sum <= 0):
    print("Suma no valida")
    quit()

nombre = input("Introduzca tu nombre: ")

while (sum > 0):
    print(nombre, end=" ")
    sum -= 1
