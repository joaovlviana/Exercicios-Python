#Verifica a quantidade de números ímpares numa lista

lista = [1,2,3,4,5,6]
qnt_total = len(lista)
lista_pares = []
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
qnt_pares = len(lista_pares)
qnt_impares = qnt_total - qnt_pares

print(f"A quantidade de números ímpares na lista é {qnt_impares}")
