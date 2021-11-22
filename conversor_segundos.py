#Converte a quantidade de segundos inserida pelo usuário em Dias-Horas-Minutos-Segundos
segundos_str = input("Insira o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // 86400
segundos_restantes = total_segs % 86400
horas = segundos_restantes // 3600
segundos_restantes_parc = segundos_restantes % 3600
minutos = segundos_restantes_parc // 60
segundos_finais = segundos_restantes_parc % 60

print(dias, "dias,", horas, "horas, ", minutos, "minutos e", segundos_finais, "segundos.")

