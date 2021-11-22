segundos = input("Insira o número de segundos que quer converter:")
dias = int(segundos) // 86400   
segundos_restantes = int(segundos) % 86400
horas = segundos_restantes // 3600
segundosRestantes = segundos_restantes % 3600
minutos = segundosRestantes // 60
segundosFinais = segundosRestantes % 60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundosFinais,"segundos.")


