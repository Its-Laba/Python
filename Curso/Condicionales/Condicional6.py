'''
    Condicional6.py
    Escribir un programa que pregunte al usuario si quiere
    una pizza vegetariana o no, y en función de su respuesta
    le muestre un menú con los ingredientes disponibles
    para que elija.
    Solo se puede eligir un ingrediente además de la mozzarella y
    el tomate que están en todas la pizzas.
    Al final se debe mostrar por pantalla si la pizza elegida es
    vegetariana o no y todos los ingredientes que lleva.
'''

vegetariana = (input("Quiere la opcion vegetariana (Y/N) : ").lower() == 'y')

if(vegetariana):
    print("Ingredientes vegetarianos: Pimiento y tofu")
    ingrediente = input("Que ingrediente adicional quieres:  ")
    if(ingrediente.lower() != "pimiento" or ingrediente.lower() != "tofu"):
        print("Error: Ingrediente no encontrado.")
        quit()
    print("Ha elegido la pizza vegetariana con mozzarella, tomate y ",ingrediente.lower())
else:
    print("Ingredientes no vegetarianos: Peperoni, Jamon y Salmon")
    ingrediente = input("Que ingrediente adicional quieres:  ")
    if(ingrediente.lower() != "peperoni" or ingrediente.lower() != "jamon" or ingrediente.lower() != "salmon"):
        print("Error: Ingrediente no encontrado.")
        quit()
    print("Ha elegido la pizza no vegetariana con mozzarella, tomate y",ingrediente.lower())
