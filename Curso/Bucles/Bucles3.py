'''
    Bucles3.py
    Escribir un programa que pida al usuario un número entero y
    muestre por pantalla un triángulo rectángulo como el de más abajo.
'''

h = int(input("¿Qué altura quieres que tenga la piramide?  "))
i = 0
brick = 0
while(i <= h):
    brick = i*2-1
    while(brick > 0):
        print(brick , end =" ")
        brick -= 2
    i += 1
    print()
