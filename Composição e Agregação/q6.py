class Comodo:
    def __init__(self,nome,tamanho):
        self.nome:str = nome
        self.tamanho:int = tamanho
class Casa:
    def __init__(self):
        self.comodos:list = []
    def adicionar_comodo(self,nome,tamanho):
        comodo = Comodo(nome,tamanho)
        self.comodos.append(comodo)
    def listar_comodos(self):
        for comodo in self.comodos:
            print(f"{comodo.nome} com {comodo.tamanho} M²")
casa = Casa()
casa.adicionar_comodo("Quarto",20)
casa.listar_comodos()

