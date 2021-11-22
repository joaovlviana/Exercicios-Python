#Função que retorna o fatorial do número inserido peli usuário

def main() :
    num = int(input("Insira o número que deseja o fatorial:"))
    fat = 1
    i = 2

    while i <= num :
        fat = fat * i
        i = i + 1
    print("O fatorial é", fat)

main()




