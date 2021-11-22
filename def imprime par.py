def imprimir_pares(n):
    lista = []
    for i in n:
        if int(i) % 2 == 0:
            lista.extend(n)
    return lista

def menu():
    n = input("Insira um valor:")
    print(imprimir_pares(n))
    print()

while True: 
    menu()
    break


    
