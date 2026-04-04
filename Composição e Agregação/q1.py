class Cidade:
    def __init__(self,nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome
    def __repr__(self):
        return f"Cidade:{self.__nome!r}"
class Pessoa:
    def __init__(self,nome,cidade):
        self.nome = nome
        self.cidade = cidade
    def __repr__(self):
        return f"Nome: {self.nome}, {self.cidade}"
class Animal:
    def __init__(self,nome,dono):
        self.nome = nome
        self.dono = dono
    def __repr__(self):
        return f"Nome: {self.nome}\nDono: {self.dono.nome}"
cidade = Cidade("CM")
pessoa = Pessoa("Arthur",cidade)
cachorro = Animal("Zeca",pessoa)
print(cidade)
print(pessoa)
print(cachorro)