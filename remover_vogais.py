#Remove as vogais de um texto digitado pelo usuário

texto = input("Insira um texto: ")
for letra in texto:
    if not (letra in 'aeiou'):
        print(letra)

