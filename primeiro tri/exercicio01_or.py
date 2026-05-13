idade = int(input("digite o tua idade: "))
ingresso_vip = input("voce tem o vip? S/N: ")
lista_convidados = input("voce esta na lista? S/N: ") 

if idade >= 18 and (ingresso_vip == "S " or lista_convidados == "S"):
    print("seja bem vindo!")



