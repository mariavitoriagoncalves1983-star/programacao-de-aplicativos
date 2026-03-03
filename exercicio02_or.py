media = float(input("digite a tua média: "))
renda = float(input("digite a sua renda familiar: "))
escola = input("voce veio de escola publica? S/N: ")

if media >= 8.0 and (renda < 2.000 or escola == "S"):
    print("ganhou a bolsa")

else: 
    print("nao atende os requesitos")