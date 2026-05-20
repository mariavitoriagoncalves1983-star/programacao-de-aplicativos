import json

cpf_aluno = int(input("Digite o teu cpf: "))
nome_completo = input("Digite o teu nome completo: ")
telefone_aluno = int(input("Digite teu telefone: "))
turma_aluno = int(input("Digite a tua turma: "))
idade_aluno = int(input("Digite a tua idade: "))


aluno = { "cpf" : cpf_aluno
          "nome" : nome_completo
          "telefone" : telefone_aluno
          "turma" : turma_aluno
          "idade" : idade_aluno
}

def cadastrar_aluno():
    with open ("escola.json", "a") as n:
        json.dump(aluno,arquivo,indent=4,ensure_ascii=False)
print("Arquivo JSON criado com sucesso!")


