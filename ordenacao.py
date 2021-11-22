#Pede para o usuário inserir três números e depois imprime se foi feito em ordem crescente ou não

num1 = int(input("Insira um número inteiro:"))
num2 = int(input("Insira um número inteiro:"))
num3 = int(input("Insira um número inteiro:"))

if (num1 <= num2 and num2 <= num3):
    print("crescente")
else:
    print("não está em ordem crescente")
