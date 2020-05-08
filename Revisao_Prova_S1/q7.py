import functools
def soma_lista(n):
    return functools.reduce(lambda a,b: a+b,[1/2**i for i in range(n)])

def calcula_limite(n):
    return [soma_lista(10**i) for i in range(n)]

print(calcula_limite(5))
