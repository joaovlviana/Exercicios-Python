#Verifica a distância entre dois pontos de um plano cartesiano

import math

x1 = float(input("Insira o valor de x1:"))
y1 = float(input("Insira o valor de y1:"))
x2 = float(input("Insira o valor de x2:"))
y2 = float(input("Insira o valor de y2:"))

dist = math.sqrt((x1-x2)**2 +(y1-y2)**2)
if dist >= 10:
    print(f"longe: {dist}")
else:
    print(f"perto:{dist}")
    
