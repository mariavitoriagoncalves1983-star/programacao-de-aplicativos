cumprimento = (input("o comprimento da peça está emtre 10 e 12 cm? S/N: "))
largura = (input("a largura esta entre 5cm e 6cm? S/N: "))

if cumprimento == "N":
    print("REPROVADO: problema no cumprimento.")
else:
    print("a largura esta entre 5cm e 6cm? S/N: ")
if largura == "S":
    print("PEÇA APROVAVA!")
else:
    print("REPROVADO: problema na largura!")