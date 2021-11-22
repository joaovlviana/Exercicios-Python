#Programa que retorna as raízes de uma equação de segundo grau e as imprime em ordem crescente

import math

a = float(input("Insira o valor de a:"))
b = float(input("Insira o valor de b:"))
c = float(input("Insira o valor de c:"))

delta = b**2 - 4*a*c


if delta == 0:
    x = (-b)/(2*a)
    print(f"a raiz desta equação é {x}")
else:
    if delta > 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        if x1>x2:
            print(f"as raízes da equação são {x2} e {x1}")
        else:
            print(f"as raízes da equação são {x1} e {x2}")
    else:
        print("esta equação não possui raízes reais")
