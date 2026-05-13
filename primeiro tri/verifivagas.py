vagas = ["Livre", "Ocupado", "Livre", "Ocupado"]
usuario = int(input("Digite a vaga de 0 a 3: "))

if 0 <= usuario < 3:
    if usuario % 2 == 0 and vagas[usuario] == "Livre": 
        print(f"Vaga {usuario} autorizada para estacionar.")
    else:
        print(f"Vaga {usuario} indisponivel das regras")
else:
    print("indice invalido")

