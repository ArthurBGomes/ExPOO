from exceptions.livro_nao_encontrado import LivroNaoEncontradoError


class Biblioteca:

    def __init__(self, nome):
        self.nome = nome
        self.catalogo_livros = []
        self.lista_membros = {}

    def adicionar_livro(self, livro):
        self.catalogo_livros.append(livro)

    def adicionar_membro(self, membro):
        self.lista_membros[membro.id_membro] = membro

    def buscar_membro_por_id(self, id_membro):
        return self.lista_membros.get(id_membro, None)

    def buscar_livro_por_isbn(self, isbn):

        for livro in self.catalogo_livros:
            if livro.isbn == isbn:
                return livro

        raise LivroNaoEncontradoError(isbn)
