nome = input("digite o teu nome: ")
idade = int(input("digite a tua idade: "))
telefone = int(input("digite teu numero de telefone:"))
motorista = input("voce possui carteira de motorista?: ")

if (nome == "joao" or "thiago" or "matheus" or "pedro" ):
    print("cancele o salvamento da lista")
if (telefone == "99999999" ):
    print("telefone inválido.")
if (idade < 0 or > 120 ):
    print("idade inválida")