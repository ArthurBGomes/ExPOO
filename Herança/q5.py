class Funcionario:
    def __init__(self,nome,salario):
        self.nome:str = nome
        self.salario:int = salario
    def exibir_dados(self):
        print(f"{self.nome} é um Funcionário que recebe salario de {self.salario:,.2f} R$")
class Gerente(Funcionario):
    def __init__(self, nome, salario,bonus):
        super().__init__(nome, salario)
        self.bonus:int = bonus
    def exibir_dados(self):
        print(f"{self.nome} é um Gerente que recebe salario de {self.salario:,.2f}R$ com um bonus de {self.bonus:,.2f}R$")
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario,linguagem):
        super().__init__(nome, salario)
        self.linguagem:str = linguagem
    def exibir_dados(self):
        print(f"{self.nome} é um Desenvolvedor {self.linguagem} que recebe salario de {self.salario:,.2f} R$")
g1 = Gerente("Arthur",10000,5000)
d1 = Desenvolvedor("Arthur",8000,"Python")
g1.exibir_dados()
d1.exibir_dados()