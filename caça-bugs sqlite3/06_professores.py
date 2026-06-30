import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close

# O erro que faltava era a vírgula no id_prof, pois ele so executa se tiver dois e para burlar o sistema tem que ter virgula