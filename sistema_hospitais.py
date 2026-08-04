import sqlite3

def conectar():
    conexao  = sqlite3.connect('hospital.db')
    conexao.execute("PRAGMA foreign_keys = ON,")
    return conexao 


def criar_tabela():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crm TEXT NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        );
        """)

        conexao.commit()
        conexao.close()


def cadastrar_hospital():
    
