class Livro:
    def __init__(self,titulo,autor):
        self.titulo:str = titulo
        self.autor:str = autor
class Biblioteca:
    def __init__(self,nome):
        self.nome:str = nome
        self.livros:list = []
    def addlivro(self,livro):
        self.livros.append(livro)
    def listar_livros(self):
        print(f"Na {self.nome} temos os seguintes livros:")
        for livro in self.livros:
            print(f"{livro.titulo} de {livro.autor}")
l1 = Livro("Noites Brancas","Fiodor Dostoiévski")
l2 = Livro("A Hora da Estrela","Clarice Lispector")
l3 = Livro("O Princíoe e o Mendigo","Mark Twin")
b1 = Biblioteca("Biblioteca dos Britos")
b1.addlivro(l1)
b1.addlivro(l2)
b1.addlivro(l3)
b1.listar_livros()