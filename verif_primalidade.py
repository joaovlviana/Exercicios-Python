#Verifica se um número inserido é primo ou não primo


n = int(input("Digite um número inteiro: "))

i = 2
x = True
while i < n:
    if n % i == 0:
        x = False
        break
    i = i + 1

if x:
    print('primo')
else:
    print('não primo')






