from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, cliente, numero, saldo,limite,tarifa_mensal):
        super().__init__(cliente, numero, saldo)
        self.__limite = limite
        self.__tarifa_mensal = tarifa_mensal
    def sacar(self,valor:float) -> float: 
        saldo_atual = getattr(self,"_ContaBancaria__saldo")
        if 0 < valor <= saldo_atual + self.__limite:
            setattr(self,"_ContaBancaria.__saldo",saldo_atual - valor)
            return True
        return False
    def cobrar_taxa(self):
        self.sacar(self.__tarifa_mensal)
    def get_tipo_conta(self):
        return "Conta Corrente"
    def exibir_dados(self):
        return f'{super().exibir_dados()}\nLimite:{self.__limite}\nTarifa:{self.__tarifa_mensal}'