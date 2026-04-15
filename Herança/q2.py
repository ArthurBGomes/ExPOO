class Animal:
    def __init__(self,grupo):
        self.grupo:str = grupo
    def __str__(self):
        return f"O Animal Pertence ao grupo dos {self.grupo}"
class Cachorro(Animal):
    def __init__(self, grupo = "Mamíferos"):
        super().__init__(grupo)
a1 = Animal("Herbívoros")
print(a1)
c1 = Cachorro()
print(c1)