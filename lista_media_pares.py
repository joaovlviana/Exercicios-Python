#Esse programa recebe o tamanho de uma lista e pede que o usuário insira os valores
#No final retorna a média da lista inserida e uma lista com apenas os números pares

tamanho = int(input("Insira o tamanho da lista:"))

i = 0
lista = []

while i < tamanho:
    i = i + 1
    num = input("Insira um número: ")
    lista.append(num)


lista_int = list(map(int, lista)) ## transformando a lista de strings em números inteiros
print(f"A lista inserida foi: {lista_int}")

lista_pares = []
for i in lista_int:
    if i % 2 == 0:
        lista_pares.append(i)

soma = 0
for j in lista_int:
    soma = soma + j

media = soma/tamanho
print(f"A média dos números da lista inserida é: {media}")


print(f"A lista de números pares fica: {lista_pares}")

