#Pede que o usuário insira seu nome e idade e retorna o nome, idade atual e a idade em 5 anos
nome = input("Digite seu nome: ").title()
idade = int(input("Digite a sua idade: "))
idade_proximo_ano = idade + 1
idade_em_5anos = idade + 5
print(f"Olá {nome}.\nVocê tem {idade} anos de idade. \nAno que vem você terá {idade_proximo_ano}. \nDaqui a 5 anos você terá {idade_em_5anos}")
