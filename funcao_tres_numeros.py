#função que recebe três número e imprime o maior

def maior_numero(a,b,c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

def menu():
    a = int(input("Insira o primeiro número:"))
    b = int(input("Insira o segundo número:"))
    c = int(input("Insira o terceiro número:"))

    print(f"O maior número é {maior_numero(a,b,c)}")
    print()
    
while True:
    menu()
    break






