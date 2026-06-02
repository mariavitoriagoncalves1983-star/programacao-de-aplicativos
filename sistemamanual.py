import json
import os

sistema_matrícula = 'sistema.json'

def cadastrar_aluno():
    print("\n--- Novo Cadastro ---")

    if os.path.exists(sistema_matrícula):
        with open(sistema_matrícula, "r", encoding='utf'-8) as n:
            sistema = json.load(n)

    else:
        sistemas = []

    novo_cadastro = {
        "id" : int(input("Id: ")),
        "nome_completo" : input("Nome_completo: "),
        "cpf" : input("CPF: "),
        "idade" : int(input("Idade: ")),
        "telefone" : input("Telefone: "),
        "turma" : input("Turma: ")
    }
    
    sistemas.append(novo_cadastro)
    with open(sistema_matrícula, "w", encoding='utf'-8) as n:
        json.dump(sistemas, n, indent=4, ensure_ascii=False)
        print("Aluno cadastrado com sucesso!")

def listar_aluno():
    print("\n--- Lista de Alunos ---")

    if os.path.exists(sistema_matrícula):
        with open(sistema_matrícula, "r", encoding='utf'-8) as n:
            sistema = json.load(n)

    else:
        sistemas = []

    if not sistemas:
        print("Erro: Este ID já está em uso!")
        return

    for sistema in sistemas:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']} ID: {aluno['id']} |")


def atualizar_aluno():
    print("\n--- Atualizar Aluno ---")

    if not os.path.exists(sistema_matrícula):
        print("Nenhum aluno cadastrado no sistema.")
        return
    
        with open(sistema_matrícula, "r", encoding='utf'-8) as n:
           sistema = json.load(n)

        id_busca = int(input("Digite o ID do aluno que deseja mudar?: "))

        for sistema in sistemas: 

            if sistema['id'] == id_busca:

                print(f"Editando dados de: {aluno['nome']}")
                aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']

                aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
                
                aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
                
                aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            
                aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']

                aluno['id'] = input(f"Novo Id ({aluno['id']}): ") or aluno['id']

        with open(sistema_matrícula, "w", encoding='utf-8') as n:
            json.dump()






            
cadastrar_aluno()