#Esse programa recebe um número n e imprime os primeiros n números ímpares 

n = int(input("Insira um número inteiro: "))

i = 1
numero_impar = 1
pa = 2

if n == 1:
    numero_impar == 1
    print(numero_impar)
else:
    while i <= n:
        print(numero_impar)
        numero_impar = numero_impar + pa
        i = i + 1


