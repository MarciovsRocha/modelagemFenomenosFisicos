import math

def calcAreaQuadrado(lado1, lado2: int):
    if lado1 <= 0 or lado2 <=0:
        print("Tipo de valor inserido eh imcompativel")
    else:
        return lado1 * lado2

def calcPerimetroRetangulo(lado1, lado2: int):
    if lado1 <= 0 or lado2 <= 0:
        print("Tipo de valor inserido eh imcompativel")
    else:
        return lado1**2 + lado2**2 

def calcAreaCirculo(r):
    if r <= 0:
        print("Valor inserido incorreto")
    else:
        return (math.pi * r ** 2)

def calcPerimetroCirculo(r):
    if r <= 0:
        print("Valor inserido incorreto")
    else:
        return 2 * math.pi * r

def calcPolinomioDef(x: int):
    return ((2*x**3) - (5*x**2)) + 1

def calcPolinomio(a,b,c,d,x: int):
    if a == 0:
        print("Valor inserido incorreto")
    else:
        return (a*x**3) + (b*x**2) + (c*x) + d

def calcAreaTriangulo(a,b,c: int):
    if a <=0 or b <=0 or c <=0:
        print("Valor inserido incorreto")
    else:
        p = (a+b+c)/2
        return math.sqrt((p*(p-a)*(p-b)*(p-c)))

def mostrarNumeroMaior(a,b: int):
    if a == b:
        print(f"São iguais {a} = {b}")
    elif a <  b:
        print(f"O primeiro numero eh maior {a}")
    else:
        print(f"O segundo numero eh maior {b}")

def comparaTresNumeros(a,b,c: int):
    if a < b and a < c:
        print(f"O maior numero eh {a}")
    elif b < a and b < c:
        print(f"O maior numero eh {b}")
    elif c < a and c < b:
        print(f"O maior numero eh {c}")
    else:
        print(f"Os numeros sao iguais {a} = {b} = {c}")


print(calcAreaQuadrado(2,4))

print(calcPerimetroRetangulo(5,10))

print(calcAreaTriangulo(5,7,3))

print(calcAreaCirculo(6))

print(calcPerimetroCirculo(9))

print(calcPolinomioDef(5))

print(calcPolinomio(4,1,4,5,16))

print(mostrarNumeroMaior(5,6))

print(comparaTresNumeros(4,6,2))
