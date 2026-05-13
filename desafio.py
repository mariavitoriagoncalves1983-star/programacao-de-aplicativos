def criar_arquivo():
    open('viagem.txt', 'w').close()

def adicionar_destino():
    destino = input("Nome do destino: ")
    with open('viagem.txt', 'a') as n:
        n.write(destino + '/n')
    print("Destino adicionado  lista!")

def listar_destino():
    with open('viagem.txt', 'r') as n:
        destinos = n.readlines()

        i = 0
        for destino in destinos:
            print(f"{i}" - {destinos.strip()})
            i += 1

def editar_destino():
    ler()
    idx = int(input("Digite o id do lugar que deseja atualizar: "))
    novo_destino = input("Novo Destino: ")

    with open('viagem.txt', 'r') as n:
        linhas = n.readlines()

    linhas[idx] = novo_destino + '/n'

    with open('viagem.txt', 'w') as n:
        f.writelines(linhas)
    print("Destino adicionado!")

def deletar_destino():
    ler()
    idx = int(input("Digite o id do lugar que deseja deletar: "))

    with open('viagem.txt', 'r') as n:
        linhas = n.readlines()

    del linhas[idx]

    with open('viagem.txt', "w") as n:
        f.writelines(linhas)
    print("Destino removido!")

while True:
    print("\n1-Adicionar destino  | 2-Listar sugestões | 3-Editar sugestão| 4-Deletar sugestão| 5-Sair")
    opcao =input("escolha uma opção: ")

    if opcao == '1': adicionar_destino()
    elif opcao == '2': listar_destino()
    elif opcao == '3': editar_destino()
    elif opcao == '4': deletar_destino()
    elif opcao == '5': 
        print("programa encerrado!")
        break 