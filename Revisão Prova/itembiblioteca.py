from abc import ABC,abstractmethod
class ItemBiblioteca(ABC):
    @abstractmethod
    def get_identificador(self):
        pass