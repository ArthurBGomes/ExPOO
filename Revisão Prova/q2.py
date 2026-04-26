from q1 import Livro,Membro
class Biblioteca:
    def __init__(self,nome):
        self.nome = nome 
        self.catalogo_livros = []
        self.lista_membros = []
    def adiocionar_livro(self,livro):
        self.catalogo_livros.append(livro)
    def adiocionar_membro(self,membro):
        self.lista_membros.append(membro)
l1 = Livro("A Hora da Estrela","Clarice Lispector",1232342343)
m1 = Membro("Arthur",1211,"email@gmail.com")
b1 = Biblioteca("Biblioteca dos Britos")
b1.adiocionar_livro(l1)
b1.adiocionar_membro(m1)
class Emprestima:
    def __init__(self,nome):
        self.livro = Livro(nome)