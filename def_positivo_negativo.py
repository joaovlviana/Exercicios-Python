#Função que recebe um número e retorna se é positivo ou negativo
def positivo_ou_negativo(num):
    if num >= 0:
        num = "positivo"
    else:
        num = "negativo"
    return num

def menu():
    num = int(input("Insira um número: "))
    print(f"O número é {positivo_ou_negativo(num)}!")
    print()

while True:
    menu()

