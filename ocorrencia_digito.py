#Pede que o usuário digite um valor e um dígito e verifica quantas vezes esse dígito está presente no valor, em seguida imprime o resultado

n = int(input("Digite o valor de n: "))
d = int(input("Digite um dígito [0,9]: "))
num = n
cont = 0
while n != 0:
    r = n % 10
    if r == d:
        cont = cont + 1
    n = n // 10
 
print(f"{d} ocorre {cont} vezes em {num}")
