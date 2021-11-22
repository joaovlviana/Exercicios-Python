#Pede que o usuário insira um número e imprime se é par/ímpar e positivo/negativo

n = int(input("Insira o número:"))

if n % 2 == 0 and n >= 0:
    print("O número é par e positivo!")
elif n % 2 == 0 and n < 0:
    print("O número é par e negativo!")
elif n % 2 != 0 and n >= 0:
    print("O número é ímpar e positivo!")
else:
    print("O número é ímpar e negativo")

