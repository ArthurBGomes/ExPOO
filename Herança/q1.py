class Computador:
    def __init__(self,processador,memoria):
        self.processador:str = processador
        self.memoria:int = memoria
    def __str__(self):
        return f"O Processador dessa máquina é o {self.processador} com memória de {self.memoria} RAM"
    
class Laptop(Computador):
    def __init__(self, processador, memoria):
        super().__init__(processador, memoria)
        self.bateria_watts = 0
class Desktop(Computador):
    def __init__(self,processador,memoria):
        super().__init__(processador,memoria)
        self.cabinete:str = ""
laptop = Laptop("Intel i5", 16)
print(laptop)

desktop = Desktop("AMD Ryzen 7", 32)
print(desktop)