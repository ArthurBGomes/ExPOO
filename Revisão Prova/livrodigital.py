from livro import Livro

class LivroDigital(Livro):
    def __init__(self, titulo, autor, isbn,formato,tamanho):
        super().__init__(titulo, autor, isbn)
        self.formato = formato
        self.tamanho_mb = tamanho
    def exibir_detalhes(self):
        return (
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"ISBN: {self.isbn} | "
            f"Formato: {self.formato} | "
            f"Tamanho: {self.tamanho_mb}MB"
        )
