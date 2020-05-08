def minimo(v):
    # criterio de parada
    # existir apenas 1 valor na lista
    if (len(v) == 1):
        return v[0]
    # calcular o menor restante da lista
    min_rest = minimo(v[1:])
    # verificando se a cabeca eh o menor valor
    if (v[0] < min_rest):
        return v[0]
    # o menor valor veio do restante da lista
    else:
        return min_rest
print(minimo([1,2,3,4]))
