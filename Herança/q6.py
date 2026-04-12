class Nadador:
    def mover(self):
        print("Nadando..")
class Corredor:
    def mover(self):
        print("Correndo..")
class TriAtleta(Nadador,Corredor):
    def mover(self):
        Nadador.mover(self)
        Corredor.mover(self)
t1 = TriAtleta()
t1.mover()