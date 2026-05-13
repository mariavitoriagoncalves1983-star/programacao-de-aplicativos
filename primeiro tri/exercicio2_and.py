media = float(input("digite a média: "))
presenca = int(input("digite a tua porcentagem de presença: ")) 

if media >= 7.0 and presenca >= 75:
    print("parabéns, você passou!")
elif media < 7.0 and presenca < 75:
    print("reprovado, verifique sua nota ou presença")