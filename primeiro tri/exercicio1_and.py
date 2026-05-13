idade = int(input("Digite a tua idade"))
dinheiro = float(input("digite o saldo que tem em sua carteira"))


if idade >= 18 and dinheiro >= 50:
    print("acesso autorizado, bem vindo ao evento! ")
  
elif idade < 18 and dinheiro < 50:
    print("infelizmente você nâo cumpre os requesitos de entrada ")
elif idade >= 18 and dinheiro < 50:
    print("infelizmente você nâo cumpre os requesitos de entrada ")
elif idade < 18 and dinheiro >= 50:
    print("infelizmente você nâo cumpre os requesitos de entrada ")