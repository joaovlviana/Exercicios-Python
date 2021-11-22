#Retorna o dígito das dezenas

x = input("Insira o número:")
aux = int(x)
div = aux % 100 # Fazendo essa divisão só nos restarão os dois últimos dígitos do número
dezena = div // 10 
print("O dígito das dezenas é", dezena)
