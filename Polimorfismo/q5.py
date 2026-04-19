class Veiculo:
     def mover(self): 
        return "Veículo se movendo"
class Moto(Veiculo):
     def mover(self): 
        return "Cortando Giro"
class Carro(Veiculo):
     def mover(self): 
        return "Catuca Railton"
class Bicicleta(Veiculo):
     def mover(self): 
        return "Pedalando"

veiculos = [Veiculo(),Moto(),Carro(),Bicicleta()]
for veiculo in veiculos:
    print(f"{veiculo.__class__.__name__}: {veiculo.mover()}")