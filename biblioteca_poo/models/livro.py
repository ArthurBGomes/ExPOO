from models.item_biblioteca import ItemBiblioteca


class Livro(ItemBiblioteca):

    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def exibir_detalhes(self):
        return (
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"ISBN: {self.isbn}"
        )

    def get_identificador(self):
        return self.isbn
