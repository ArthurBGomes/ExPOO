from abc import ABC,abstractmethod
import math 
class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
class Circulo(FormaGeometrica):
    def __init__(self,raio):
        self.raio:int = raio
    def calcular_area(self):
        return math.pi * self.raio**2
class Retangulo(FormaGeometrica):
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    def calcular_area(self):
        return self.altura * self.largura
class Triangulo(FormaGeometrica):
    def __init__(self,base,altura):
        self.base = base 
        self.altura = altura 
    def calcular_area(self):
        return (self.base * self.altura) / 2
areas = [Circulo(6),Retangulo(12,16),Triangulo(12,9)]
for area in areas:
    print(f"{area.__class__.__name__}: {area.calcular_area():.2f}")