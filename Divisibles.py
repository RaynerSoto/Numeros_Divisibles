def divisibles(x):
    valor_inicial = 2
    arreglo = list()
    if x < 0 :
        valor_inicial = -2
    for i in range(valor_inicial,x):
        if x % i == 0:
            arreglo.append(i)
    return arreglo

def resultado(x):
    arreglo = divisibles(x)
    if len(arreglo) == 0:
        print('Es un número primo')
    else:
        print(arreglo)

