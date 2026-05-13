seguranca = input("Voce concluiu o curso de segurança? S/N:  ")


if seguranca == "S":
    instrutor = input("o instrutor esta presente na sala? S/N: ")
    if instrutor == "S":
        print("acesso liberado! operação iniciada.")
    else:
        print("aguarde o instrutor para ligar a máquina.")

else:
    print("acesso negado! faça o treinamento primeiro.")