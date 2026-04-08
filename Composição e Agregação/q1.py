class Cidade:
    def __init__(self,nome):
        self.__nome:str = nome
    @property
    def nome(self):
        return self.__nome
    def __str__(self):
        return f"Cidade:{self.__nome}"
class Pessoa:
    def __init__(self,nome,cidade):
        self.nome:str = nome
        self.cidade:str = cidade
    def __str__(self):
        return f"Nome: {self.nome}, {self.cidade}"
class Animal:
    def __init__(self,nome,dono):
        self.nome = nome
        self.dono = dono
    def __str__(self):
        return f"Nome: {self.nome}\nDono: {self.dono.nome}"
cidade = Cidade("CM")
pessoa = Pessoa("Arthur",cidade)
cachorro = Animal("Zeca",pessoa)
print(cidade)
print(pessoa)
print(cachorro)