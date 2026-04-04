class Jogador:
    def __init__(self,nome,posicao):
        self.nome = nome
        self.posicao = posicao
class Time:
    def __init__(self,nome):
        self.nome = nome
        self.jogadores = []
    def adicionar_jogador(self,jogador):
        self.jogadores.append(jogador)
    def listar_jogadores(self):
        for jogador in self.jogadores:
            print(f"{jogador.nome} - {jogador.posicao}")
j1 = Jogador("Arthur","Zagueiro")
j2 = Jogador("Ana","Atacante")
j3 = Jogador("Rafaela","Goleira")
t1 = Time("Britos'Fc")
t1.adicionar_jogador(j1)
t1.adicionar_jogador(j2)
t1.adicionar_jogador(j3)
t1.listar_jogadores()