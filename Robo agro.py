nb = int(input("Digite o nível de bateria (0-100): "))
t = float(input("Digite a temperatura ambiente (em °C): "))
um = int(input("Digite a umidade do solo (0-100): "))
mo = input("Digite o modo de operação:\nPlantio\nColheita\nIrrigação\nDigite aqui: ")
modo = mo.lower
tst = 0

if nb > 50:
    print("Bateria suficiente para operação.")
else:
    if nb >= 20:
        print("Atenção: bateria em nível moderado.")
    else:
        print("Bateria muito baixa! Retorne imediatamente para a base.")

if t > 40:
    print("Temperatura crítica! Operação suspensa.")
else:
    if t < 5:
        print("Frio extremo! Modo de economia ativado.")
    else:
        print("Temperatura adequada para trabalho!")

if um < 30:
    print("Solo muito seco. Recomendado iniciar irrigação.")
else:
    if um > 80:
        print("Solo encharcado! Suspenda irrigação imediatamente.")
    else:
        print("Nível de umidade dentro do ideal. Perfeito para o desenvolvimento!")

if nb > 50:
    tst +=1
if t <= 35:
    if t >= 10:
        tst += 1
if um <= 80:
    if um >= 30:
        tst += 1

if tst != 3:
    print("Operação negada! Verifique as condições do ambiente.")
else:
    print("Robô autorizado a iniciar a operação!")
    print(f"Iniciando modo {modo}!")