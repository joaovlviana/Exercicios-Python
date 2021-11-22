#Verifica se a senha foi digitada corretamente e retorna o resultado

senha = "12345"
login = input("Insira a senha: ")

i = 5
j = len(login)
k = i - j
if j < i:
    input(f"Faltam {k} letras")
else:
    if login == senha:
        input("ACESSO PERMITIDO ")
    else:
        input("ACESSO NEGADO ")


