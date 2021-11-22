numero = int(input("Insira um número: "))
tamanho = len(str(numero))

i = 1
x = True
aux = -1
while i <= tamanho:
    aux2 = aux
    aux = numero % 10
    numero = numero // 10
    if aux2 == aux:
        x = False
        break
    else:
        i = i + 1

if x:
    print("não")
else:
    print("sim")

