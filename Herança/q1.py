class Computador:
    def __init__(self,processador,memoria):
        self.processador:str = processador
        self.memoria:int = memoria
class Laptop(Computador):
    def __init__(self, processador, memoria):
        super().__init__(processador, memoria)
        self.bateria_watts = 0
class Desktop(Computador):
    def __init__(self,processador,memoria):
        super().__init__(processador,memoria)
        self.cabinete:str = ""