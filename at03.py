def soma_lista(numeros, *args):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

print(soma_lista([1,2,3,4]))