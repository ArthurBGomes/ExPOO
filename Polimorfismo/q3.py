class Animal:
    def emitir_som(self):
        return "Um Som Desconhecido"
class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"
class Gato(Animal):
    def emitir_som(self):
        som = super().emitir_som()
        print(f"Som da superclasse: {som}")
        return "Miado"

animais =[Animal(),Cachorro(),Gato()]
for animal in animais:
    print(f"{animal.__class__.__name__}: {animal.emitir_som()}")