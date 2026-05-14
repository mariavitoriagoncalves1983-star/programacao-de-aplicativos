def criar_arquivo():
    open('habitos.txt', 'w').close()

def cadastar_habito():
    inserir = input("Digite teu novo habito: ")
    with open('habitos.txt', 'a') as n:
        n.write(inserir + '/n')
        print("Novo habito cadastrado!")

def revisar_mural():
    with open('habitos.txt', 'r') as n:
        revisados = n.readlines()

        m = 0
        for revisado in revisados:
            print(f"/n{m} - {revisado.strip()}")
            m += 1

def editar():
    ler()
    idx = int(input("Digite o id do habito que deseja mudar: "))
    novo_habito = input("Novo habito: ")

    with open('habitos.txt', 'r') as n:
        linhas = f.readlines

    linhas[idx] = novo_habito + '/n'

    with open('habitos.txt', 'w') as n:
        n.writelines(linhas)
        print("Habito atualizado!")

    def descartar_habito():
        ler()
        idx = int(input("Digite o ID do habito que deseja excluir: "))

        with open('habitos.txt', 'r') as n:
            linhas = n.readlines

            del linhas[idx]

        with open('habitos.txt', 'w') as n:
            n.writelines(linhas)
        print("Lugar removido!")   

while True:
    print("/n1 - cadastrar")
    print("/n2 - revisar ")
    print("/n3 = editar")
    print("/n4 - descartar")
    print("/n5 - sair ")

    opcao = input("Escolha: ")

    if opcao == '1': cadastar()
    elif opcao == '2': revisar()
    elif opcao == '3': editar
    elif opcao == '4': sair
    elif opcao == '5':
        print("Programa encerrado!")
        break



    

