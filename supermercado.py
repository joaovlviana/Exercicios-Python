item = input("Insira o item: ")
preco = float(input("Insira o preço do produto: "))
quantidade = int(input("Insira a quantidade: "))
total = preco*quantidade

print('{} ({} unidades): R$ {}'.format(item, quantidade, total))