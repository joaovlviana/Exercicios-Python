#Função que múltiplica os números de uma lista
def mult_lista(numeros):
    valor = 1
    for i in numeros:
        valor = valor * i
    return valor

print(mult_lista([2,3]))
