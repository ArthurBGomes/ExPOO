class Veiculo:
     def acelerar(self): 
          print("acelerando")
class Moto(Veiculo):
     def acelerar(self): 
          print("Cortando Giro")
class Carro(Veiculo):
     def acelerar(self): 
          print("Catuca Railton")

v1 = Veiculo()
v1.acelerar()
m1 = Moto()
m1.acelerar()
c1 = Carro()
c1.acelerar()