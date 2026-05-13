salario = float(input("digite o teu salario: "))
if salario >= 10000:
    print("rico: ")
elif salario >= 5000:
    print("classe média: ")
elif salario < 5000:
    print("classe baixa: ")