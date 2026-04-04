class Autor:
    def __init__(self,autor):
        self.autor = autor
class Livro:
    def __init__(self,nome,autor):
        self.nome = nome
        self.autor = Autor(autor)
    def mostrar_livro(self):
        print(f"o Livro:{self.nome} do autor {self.autor.autor}")
l1 = Livro("O Homem Que Calculava","Malba Tahan")
l1.mostrar_livro()