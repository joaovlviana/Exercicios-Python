#Pede que o usuário digite uma sequencia de valores e retorna a soma

print("Digite uma sequência de valores terminada em zero. ")
soma = 0

valor = 1
while valor != 0:
    valor = float(input("Digite um valor a ser somado: "))
    soma = soma + valor

print(f"A soma dos valores digitados é {soma}")
