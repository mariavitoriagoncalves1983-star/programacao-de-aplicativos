valor_compra = float(input("digite o valor da sua compra: "))
prime_assinatura = input("voce é prime? S/N: ")
frete = 50.00

if valor_compra > 500.00 or (prime_assinatura == "S" and valor_compra > 100.00):
    frete = 00.00
    print("Parabens ganhou frete grátis!")
    valor_compra + frete
    print("teu valor totl é", valor_compra + frete)

else:
    frete = 50.00
    valor_compra + frete
    print("voce nao ganhou o frete grátis")
    