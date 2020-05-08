import functools
# funcao para calcular fatorial de um numero 'x'
def fat(x):
    if (x < 0):
        return -1
    if ((x == 0) or (x == 1)):
        return 1
    else:
        return x*fat(x-1)

 
soma = lambda n: functools.reduce(lambda x,y: x+y,n)
q4_1 = soma([1/i for i in range(1,10)])
q4_2 = soma([1/i for i in range(1,11,+2)])
q4_3 = soma([1/fat(i) for i in range(10)])
q4_4 = soma([(1/(2**i)) for i in range(10)])

print(q4_1)
print(q4_2)
print(q4_3)
print(q4_4)
