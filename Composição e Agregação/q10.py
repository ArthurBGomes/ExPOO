class Aluno:
    def __init__(self,nome):
        self.nome = nome
class Turma:
    def __init__(self,nome):
        self.nome = nome
        self.alunos = []
    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)
    def exibir_alunos(self):
        print(f"os alunos da turma {self.nome}:")
        for aluno in self.alunos:
            print(aluno.nome)
class Escola:
    def __init__(self,nome):
        self.nome = nome
        self.turmas = []
    def adicionar_turma(self,nome):
        turma = Turma(nome)
        self.turmas.append(turma)
    def exibir_turmas(self):
        print(f"as turmas da Escola {self.nome}:")
        for turma in self.turmas:
            print(turma.nome)
a1 = Aluno("Arthur")
a2 = Aluno("Rafinha")
a3 = Aluno("Giovanna")
a4 = Aluno("George")
t1 = Turma("INFO2V")
t1.adicionar_aluno(a1)
t1.adicionar_aluno(a2)
t1.adicionar_aluno(a3)
t1.adicionar_aluno(a4)
t1.exibir_alunos()
e1 = Escola("IFRN")
e1.adicionar_turma(t1.nome)
e1.exibir_turmas()
