nome_do_cliente = input("digite o teu nome: ")
valor_total = float(input("digite o total d compra: "))
distancia = int(input("digite a distância em km: "))
cupom_especial = input("cupom especial? digite S ou N: ")
frete = 40.00
total = 0.00

if valor_total >= 1000.00 and cupom_especial == "S":
    desconto = 0.20 * valor_total
    total = valor_total - desconto
    print("parabéns! você ganhou um mouse pad Gamer de brinde!")

elif valor_total > 500.00 and valor_total < 1000.00 and cupom_especial == "S":
    desconto = 0.10 * valor_total
    total = valor_total - desconto 


if distancia <= 50 and total > 200.00:
    frete = 0.00
    valor_final = total + frete
 
else:
    valor_final = total + frete 



    print("nome do cliente: ", nome_do_cliente)
    print("valor original", valor_total)
    print("valor do desconto apliicado", desconto)
    print("valor final a pagar", valor_final)

