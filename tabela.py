import sqlite3

def criar():
    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores (
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                nome completo TEXT NOT NULL,
                telefone TEXT,
                materia TEXT,
                idade INTERGER,
                cpf TEXT UNIQUE NOT NULL
                salario REAL,
                escola TEXT,
                )
                ''')

    nome_completo = input("Digite o nome do professor: ")
    telefone = input("Digite o telefone do professor: ")
    materia = input("Digite a materia do professor: ")
    idade = int(input("Digite a idade do professor: "))
    cpf = input("Digite o cpf do professor: ")
    salario = input("Digite o salario do professor: ")
    escola = input("Digite a escola do professor: ")

    comando_inserir = f'''
            INSERT INTO  alunos (nome, telefone, materia, idade, cpf, salario, escola)
            values ('{nome_completo}', '{telefone}', '{materia}', '{idade}', '{cpf}', '{salario}', '{escola}')
            '''

    cursor.execute(comando_inserir)

    conexao_commit()

    print("cadastro realizado!")

    conexao.close()


def listar():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professores")
    professores = conexao.fetchall()

    print("=== Lista de Professor ===")

    for aluno in alunos:
        

