class Cidade:
    def __init__(self,nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome
    def __repr__(self):
        return f"Cidade({self.__nome!r})"
class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        self.cidade = Cidade()
class Animal:
    def __init__(self,nome):
        self.nome = nome
        self.dono = Pessoa()