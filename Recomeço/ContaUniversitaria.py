from Recomeço.ContaBancária import ContaBancaria
from rich import print,inspect
class ContaUniversitaria(ContaBancaria):
    def __init__(self, cliente, numero, saldo):
        super().__init__(cliente, numero, saldo)
        self.__limite = 500.00
    
    def sacar(self,valor):
        if self.get_saldo() + self.__limite > valor:
            self.set_saldo(self.get_saldo() - valor)
            return True
        else:
            print("Saldo/Limite Insuficiente")
            return False
    def get_tipo_conta(self):
        return "Conta Universitária"
cu1 = ContaUniversitaria("Fulano","1001",1000)
cu1.sacar(1200)
inspect(cu1,private=True)
