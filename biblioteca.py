class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


    def exibirInfos(self):
        situacao = "Disponivel" if self.disponivel else "Indisponivel"
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Situação: {situacao}")


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []


    def emprestarLivro(self, livro,):
        if livro.disponivel:
            livro.disponivel = False
            self.livrosEmprestados.append(livro)
            print(f"{self.nome} emprestou o livro {livro.titulo}.")
        else:
            print(f"O livro {livro.titulo} ja está emprestado.")


    def devolverLivro(self, livro):
        if livro in self.livrosEmprestados:
            livro.disponivel = True
            self.livrosEmprestados.remove(livro)
            print(f"{self.nome} devolveu o livro {livro.titulo}.")
        else:
            print(f"{self.nome} não possui o livro {livro.titulo}.")


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []


    def adicionarLivros(self, livro):
        self.livros.append(livro)
        print(f"Livro {livro.titulo} foi adicionado a biblioteca.")


    def exibirLivrosDisponiveis(self):
        print(f"Livros disponiveis na {self.nome}:")
        for livro in self.livros:
            if livro.disponivel:
                livro.exibirInfos()

        print()


biblioteca = Biblioteca("Biblioteca")
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("A Metamorfose", "Franz Kafka")
livro3 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling")
biblioteca.adicionarLivros(livro1)
biblioteca.adicionarLivros(livro2)
biblioteca.adicionarLivros(livro3)

usuario = Usuario("Victor")
biblioteca.exibirLivrosDisponiveis()

usuario.emprestarLivro(livro1)
usuario.emprestarLivro(livro3)
biblioteca.exibirLivrosDisponiveis()

usuario.devolverLivro(livro1)
biblioteca.exibirLivrosDisponiveis()