#Soma os dígitos do número inserido

n = int(input("Digite um número inteiro: "))

soma = 0

while n > 0:
    soma = soma + n % 10 #Soma o útimo dígito à variável soma
    n = n // 10 #Remove o último número de n

print(soma)




