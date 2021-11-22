for numero in range(1,51):
    if numero % 3 == 0 and numero % 5 == 0:
        print(numero,"DELTAOMEGA")
    elif numero % 5 == 0 and numero % 3 != 0:
        print(numero,"OMEGA")
    elif numero % 3 == 0 and numero % 5 != 0:
        print(numero,"DELTA")

