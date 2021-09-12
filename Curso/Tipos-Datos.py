# Como todo lenguaje de programacion existen los tipos de datos
# Python es especial ya que no hay que decir el tipo para inicializarlos
#
# Pero aqui estara la lista de tipos de datos en caso de que los necesite

# Datos numericos

int = 3      # enteros

binario = 0b1010 # para numeros binarios se escribe antes '0b'
octal = 0o12 # para numeros octales se escribe antes '0o'
hex = 0xa    # para numeros hexadecimales se escribe antes '0x'

float = 3.14 # flotantes o reales

# Para numeros imaginarios se utiliza .imag
complejo = 1 + 2j

complejo.real # devuelve el valor real
complejo.imag # devuelve el valor imaginario

# Booleanos

bool = True # booleanos
# Ciertos objetos son considerados como False
# None; False; Cualquier valor 0; Cualquier lista vacia

# Caracteres

char = 'c'  # letras
string = "Hola mundo" # cadenas de letras

# Otros tipos

# listas: conjuntos mutables de valores
lista = [1,2,3,2]
# tupla: conjuntos inmutables de valores
tupla = (1,2,3,4)
# conjunto: representar conjuntos unicos de elementos (no puede haber ningun repe)
conjunto = set([1,2,3,4]) # set
# diccionarios: tipos de contenedores en los que s epuede acceder a sus elementos
#               por medio de una clave unica
diccionarios = {'a': 1, 'b': 2, 'c': 3} # dict

# Para conocer el tipo de una variable se puede utilizar:
#   type() : devuelve el tipo de la variable
#   isinstance(var,type) : devuelve True si la var corresponde con type

# Conversion de tipos

int() # para pasar a entero
str() # para pasar a string
float() # para pasar a reales
complex() # para pasar a complejo
