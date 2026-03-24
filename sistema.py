autorizados = ["Alice", "Bob", "Carlos"]
nome = input("Digite o nome do pesquisador: ")

if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {indice}")

    remover = input("Deseja remover esse pesquisador da lista? S/N: ")
    if remover == "S":
        autorizados.remove(nome)
        print(f"lista atualizada: {autorizados}")
    else:
        print("saindo da lista...")

else:
    print(f"Acesso Negado! O pesquisador {nome} não foi encontrado.")
    cadastrar = input("Você deseja cadastrar esse novo pesquisador? S/N: ")

    if cadastrar == "S":
        autorizados.append(nome)
    print(f"lista atual: {autorizados}")