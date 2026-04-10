class Animal:
    def __init__(self,grupo):
        self.grupo:str = grupo
class Cachorro(Animal):
    def __init__(self, grupo):
        super().__init__(grupo)
        self.grupo = "Mamífero"
