# importar arquivos
import json
import os

# variavel de alunos
BANCO_DADOS = 'alunos.json'

# funcao cadastrar os alunos
def cadastrar():

    # mostra no terminal
    print("\n--- Novo Cadastro ---")
    
    # verifica se o arquivo existe
    if os.path.exists(BANCO_DADOS):

        # abrindo a funcao de ler o arquivo
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

            # lendo arquivo
            alunos = json.load(f)

    # se nao, criar uma nova lista        
    else:
        alunos = []

    # criaçao do objeto
        novo_aluno = { # abrir chave do objeto
        "nome": input("Nome: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    } # fechar chave do objeto

    # adicionar os alunos ao objeto
    alunos.append(novo_aluno)

    # abrindo a funçao de escrever
    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:

        # escreve no arquivo
        json.dump(alunos, f, indent=4, ensure_ascii=False)
    
    # mostrar ao terminal 
    print("Aluno cadastrado com sucesso!")

# funcao listar alunos
def listar():

    # mostrar ao terminal
    print("\n--- Lista de Alunos ---")
    
    # se o arquivo existir
    if os.path.exists(BANCO_DADOS):

        # abrindo o arquivo
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

            # lendo o arquivo 
            alunos = json.load(f)

    # se nao existir alunos      
    else:
        alunos = []

    # se nao for alunos 
    if not alunos:
         
        # mostre nenhum aluno cadastrado
        print("Nenhum aluno cadastrado.")

        # retorne
        return

    # se oque a pessoa digitou estiver na lista 
    for aluno in alunos:

        # mostre o nome, cpf, turma, telefone
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")

# funcao atualizar o aluno
def atualizar():

    # abrir no terminal 
    print("\n--- Atualizar Aluno ---")

    # se nao existir no banco de dados
    if not os.path.exists(BANCO_DADOS):

        # mostre que nao tem aluno cadastrado
        print("Nenhum aluno cadastrado no sistema.")

        # retorne
        return

    # abrindo arquivo para ler
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

        # lendo arquivo
        alunos = json.load(f)

    # variavel de cpf para editar o antigo 
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: "))
    
    # se nome dito, percorra a lista
    for aluno in alunos:

        # se cpf do aluno for igual o cpf da busca
        if aluno['cpf'] == cpf_busca:

            # editando dados do aluno que foi pedido
            print(f"Editando dados de: {aluno['nome']}")

            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            # cadastrando novo nome do aluno, ou deixando nome antigo

            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            # cadastrando novo telefone do aluno, ou deixando telefone antigo

            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            # cadastrando novo turma do aluno, ou deixando turma antigo

            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            # cadastrando novo idade do aluno, ou deixando idade antigo

            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            # cadastrando novo cpf do aluno, ou deixando cpf antigo
            

            # abrindo arquivo para sobreescrever
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:

                # escrevendo arquivo
                json.dump(alunos, f, indent=4, ensure_ascii=False)

            # mostrando que os dados foram atualizados
            print("Dados atualizados com sucesso!")

            # retorne
            return

    # mostrando que nao tem aluno encontrado
    print("Aluno não encontrado.")

# funcao excluir aluno
def excluir():

    # moatrando que aluno vai ser excluido
    print("\n--- Excluir Aluno ---")

    # se nao existir
    if not os.path.exists(BANCO_DADOS):
  
        # mostrando que nao tem aluno cadastrado
        print("Nenhum aluno cadastrado no sistema.")

        # retorne
        return

    # abrindo arquivo para ler
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

        # lendo arquivo
        alunos = json.load(f)
    
    # nova variavel de remover aluno
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    # nova lista
    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        
        # mostrando que aluno foi removido
        print("Aluno removido com sucesso!")

    # se nao, mostre que nao tem aluno encontrado
    else:
        print("Aluno não encontrado.")

# funcao 
def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        # variavel de escolha de opcao 
        opcao = input("Escolha uma opção: ")
        
         if opcao == '1': cadastrar()
        # se opcao escolhida for 1, mostre cadastrar

        elif opcao == '2': listar()
        # se nao. se escolhida 2, mostre listar

        elif opcao == '3': atualizar()
        # se nao. se escolhida 3, mostre atualizar

        elif opcao == '4': excluir()
        # se nao. se escolhida 4, mostre excluir
        
        elif opcao == '5': break
        # se nao. se escolhida 5, quebrar codigo

        else: print("Opção inválida!")
        # se nao, mostre opcao invalida 

menu()



        



