#Calcula a média dos números de uma lista

tamanho = int(input("Insira o tamanho da amostra:"))

i = 0
lista = []

while i < tamanho:
    i = i + 1
    num = input("Insira um número: ")
    if num == "" :
        num = "0"
    else:
        num
    lista.append(num)


lista_int = list(map(int, lista))
print(lista_int)


def somar_lista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

print(somar_lista(lista_int))
soma = somar_lista(lista_int)
media = soma/tamanho
print(f"A média dos elementos da lista é {media}")









