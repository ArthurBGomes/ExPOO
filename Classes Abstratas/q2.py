from abc import ABC,abstractmethod
class DispositivoEletronico(ABC):
    def __init__(self):
        self.ligado = False
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
class Carregavel(ABC):
    def __init__(self):
        self.carregado = False
    def carregar(self):
        pass
class Smartphone(DispositivoEletronico,Carregavel):
    def __init__(self):
        DispositivoEletronico.__init__(self)
        Carregavel.__init__(self)
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return "o dispositivo está ligado"
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return "o dispositivo está desligado"
    def carregar(self):
        self.carregado = True
        if self.carregado:
            return "O Dispositivo está carregado"
class Notebook(DispositivoEletronico,Carregavel):
    def __init__(self):
        DispositivoEletronico.__init__(self)
        Carregavel.__init__(self)
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return "o dispositivo está ligado"
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return "o dispositivo está desligado"
    def carregar(self):
        self.carregado = True
        if self.carregado:
            return "O Dispositivo está carregado"
    
class FoneDeOuvido(DispositivoEletronico):
    def __init__(self):
        super().__init__()
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return "o dispositivo está ligado"
    def desligar(self):
        if self.ligado:
            self.ligado = False
            return "o dispositivo está desligado"
dispositivos = [Smartphone(), Notebook(), FoneDeOuvido()]
carregaveis  = [Smartphone(), Notebook()]

print("=== Dispositivos Eletrônicos ===")
for d in dispositivos:
    nome = d.__class__.__name__
    print(f"{nome} → {d.ligar()}")
    print(f"{nome} → {d.desligar()}")

print("=== Carregáveis ===")
for c in carregaveis:
    nome = c.__class__.__name__
    print(f"{nome} → {c.carregar()}")