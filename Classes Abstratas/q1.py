from abc import ABC,abstractmethod
class Controlavel(ABC):
    @abstractmethod
    def mover(self):
        pass
class Jogador(Controlavel):
    def mover(self):
        print("Jogador se movendo")
class Volante(Controlavel):
    def mover(self):
        print("Volante girando")
j1 = Jogador()
v1 = Volante()
j1.mover()
v1.mover()