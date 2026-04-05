class Processador:
    def __init__(self,modelo,velocidade):
        self.modelo:str = modelo
        self.velocidade:float = velocidade
class Memoria:
    def __init__(self,capacidade):
        self.capacidade:int = capacidade
        
class Computador:
    def __init__(self,modelo,velocidade,capacidade):
        self.processador = Processador(modelo,velocidade)
        self.memoria = Memoria(capacidade)
    def exibir_configurações(self):
        print(f"Processador:{self.processador.modelo} com {self.processador.velocidade} Ghz e com {self.memoria.capacidade} GB de Memória RAM ")
pc = Computador("Ryzen 7",3.4,16)
pc.exibir_configurações()