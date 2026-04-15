class Motor: 
    def __init__(self,potencia):
        self.potencia:int = potencia
        self.motor:str = "Combustão"
        self.ligado:bool = False
    def liga_desliga(self):
        if not self.ligado:
            self.ligado = True
            print(f"Motor de {self.motor} de {self.potencia} cavalos Ligando...")
        else:
            self.ligado = False
class MotorEletrico(Motor):
    def __init__(self, potencia):
        super().__init__(potencia)
        self.motor:str = "Energia"
class Carro:
    def __init__(self,modelo,potencia):
        self.modelo = modelo
        self.motor = Motor(potencia) # Nessa linha, criamos um objeto da classe motor,e a partir disso,conseguimos acessar todos os seus métodos
    def liga_desliga(self):          # self →  o objeto Carro
        self.motor.liga_desliga()    # self.motor    →  o objeto Motor que está dentro do Carro
                                     # self.motor.liga_desliga()  →  chama o método liga_desliga() desse Motor

class CarroEletrico(Carro):
    def __init__(self,modelo, potencia):
        super().__init__(modelo,potencia)
        self.motor = MotorEletrico(potencia)
c1 = Carro("Civic",250)
c1.liga_desliga()
ce1 = CarroEletrico("Tesla",300)
ce1.liga_desliga()