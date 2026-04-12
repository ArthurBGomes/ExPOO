class Motor: 
    def __init__(self,potencia):
        self.potencia:int = potencia
        self.ligado:bool = False
    def liga_motor(self):
        if not self.ligado:
            self.ligado = True
            print(f"Motor de {self.motor} de {self.potencia} cavalos Ligando...")
        else:
            self.ligado = False
class Eletrico:
    def __init__(self):
        self.bateria:str = "Descarregado"
    def carregar(self):
        self.bateria = "Carregado"
class Combustão:
    def __init__(self,):
        self.tanque:str = "Vazio"
    def carregar(self):
        self.tanque = "Cheio"
class CarroEletrico(Motor,Eletrico):
    def __init__(self, potencia):
        super().__init__(potencia)
class CarroHibrido(Motor,Eletrico,Combustão):
    def __init__(self, potencia):
        super().__init__(potencia)
