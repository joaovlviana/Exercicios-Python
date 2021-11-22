#Pede que o usuário insira um número e, se o mesmo for divisível por 5, imprime "Buzz", caso contrário imprime o próprio número.
num = int(input("Insira um número inteiro:"))

if num % 5 == 0 :
    print("Buzz")
    
else :
    print(num)
