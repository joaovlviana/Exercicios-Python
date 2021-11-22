def texto_invertido(txt):
    return txt[::-1]

def menu():
    txt = input("Insira um texto:")
    print(f"O texto invertido fica {texto_invertido(txt)}")
    print()

while True:
    menu()
    break

