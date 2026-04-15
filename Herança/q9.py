class Motor: 
    def __init__(self,potencia):
        self.potencia:int = potencia
        self.ligado:bool = False
    def liga_motor(self):
        if not self.ligado:
            self.ligado = True
            print(f"Motor de {self.potencia} cavalos Ligando...")
        else:
            self.ligado = False
    def exibir_info(self):
        print(f"Motor de: {self.potencia} cv")
class Eletrico:
    def __init__(self,bateria):
        self.bateria:int = bateria
    def carregar(self):
        print(f"Carregando bateria de {self.bateria} Kwh")
    def exibir_info(self):
        print(f"Bateria de {self.bateria} Kwh")
class Combustão:
    def __init__(self,tanque):
        self.tanque:int = tanque
    def carregar(self):
        print(f"Abastecendo tanque de {self.tanque} L")
    def exibir_info(self):
        print(f"Tanque de {self.tanque} L ")
class CarroEletrico(Motor,Eletrico):
    def __init__(self, potencia,bateria):
        Motor.__init__(self,potencia)
        Eletrico.__init__(self,bateria)
    def exibir_info(self):
        print(f" Carro Elétrico com:")
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)
class CarroHibrido(Motor,Eletrico,Combustão):
    def __init__(self, potencia,bateria,tanque):
        Motor.__init__(self,potencia)
        Eletrico.__init__(self,bateria)
        Combustão.__init__(self,tanque)
    def exibir_info(self):
            print(f" Carro Híbrido com:")
            Motor.exibir_info(self)
            Eletrico.exibir_info(self)
            Combustão.exibir_info(self)
ce = CarroEletrico(200,50)
ce.liga_motor()
ch = CarroHibrido(250,60,50)
ch.liga_motor()
ce.exibir_info()
ch.exibir_info()
