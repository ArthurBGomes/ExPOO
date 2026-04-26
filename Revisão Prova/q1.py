class Livro:
    def __init__(self,titulo,autor,isbn):
        self.titulo:str = titulo
        self.autor:str = autor
        self.isbn:int = isbn
    def exibir_detalhes(self):
        print(f"o Livro {self.titulo!r} de {self.autor} com código ISBN:{self.isbn}")
class Membro:
    def __init__(self,nome,id_membro,contato):
        self.nome:str = nome
        self.id_membro:int = id_membro
        self.contato:str = contato
l1 = Livro("A Hora da Estrela","Clarice Lispector",1232342343)
l1.exibir_detalhes()