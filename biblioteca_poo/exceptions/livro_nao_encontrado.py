class LivroNaoEncontradoError(Exception):
    def __init__(self, isbn):
        super().__init__(f"Livro com ISBN {isbn} não encontrado.")
