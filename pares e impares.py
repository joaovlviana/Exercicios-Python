n = int(input("Insira o número de algarismos da sequência:"))

i = 1
j = 0
k = 0

while n >= i :
    n = n - i
    x = int(input("Insira um número: "))
    if x % 2 == 0:
        j = j + 1
    else:
        k = k + 1

    
print(f"A quantidade de números pares é {j} e de números ímpares é {k}")


