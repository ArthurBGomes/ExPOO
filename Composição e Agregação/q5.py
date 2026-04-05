class Professor:
    def __init__(self,nome,titulacao):
        self.nome = nome
        self.titulacao = titulacao
class Disciplina:
    def __init__(self,nome,professor):
        self.nome = nome
        self.professor =[ professor]
    def exibir_informações(self):
        for disciplina in self.professor:
            print(f"Professor:{disciplina.nome},Disciplina:{self.nome}")

p1 = Professor("Patrão Léo","Doutor")
d1 = Disciplina("Programação",p1)
d1.exibir_informações()