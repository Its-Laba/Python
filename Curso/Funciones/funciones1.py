'''
    Funciones1.py
    Script para escribir funciones y trastear un poco
'''

# Funcion Fibonacci (imprime la sucesión de n números)
def fib(n: int):
    '''
        Imprime la sucesión de Fibonacci hasta el n elemento
    '''
    a, b = 0 ,1
    c = 0
    if(n == 1):
        print(a)
        return
    print(f"{a} {b}", end = " ")
    n -= 2
    while(n > 0):
        n -= 1
        c = a + b
        a = b
        b = c
        print(c, end = " ")

def concat(*args, sep = "/"):
    return sep.join(args)
print(concat("User","Lucas","Descargas"))
print(concat("User","Lucas","Descargas", sep = "."))

print(fib.__doc__)
print(fib.__annotations__)
