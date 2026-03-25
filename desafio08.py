livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []

livros = input("Digite o nome do livro que deseja: ")

if livros in livros_disponiveis:
    livros_disponiveis.remove(livros)
    livros_emprestados.append(livros)
    print("Empréstimo realizado com sucesso!")
else:
    ("Desculpe, este livro não está no acervo.")

livro_emprestado = input("Digite o nome do livro para devolução: ")
if livro_emprestado in livros_emprestados:
    livros_emprestados.remove(livro_emprestado)
    livros_disponiveis.append(livro_emprestado)
    print("livro devolvido com sucesso!")
else:
    print("este livro não consta como emprestado...")

del livros_disponiveis [0:2]
print(f"estado final das duas listas, disponiveis: {livros_disponiveis} e emprestados: {livros_emprestados}")