#Exemplo de criação de função para somar uma sequência de números inserida pelo usuário terminada em zero
def main():
    num = int(input("Digite um inteiro: "))
    soma = 0

    while num != 0:
        soma = soma + num
        num = int(input("Digite um inteiro: "))

    print("A soma é", soma)


#----------------------------------------------
main()
