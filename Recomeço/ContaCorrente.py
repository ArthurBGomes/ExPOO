from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, cliente, numero, saldo,limite,tarifa_mensal):
        super().__init__(cliente, numero, saldo)
        self.__limite = limite
        self.__tarifa_mensal = tarifa_mensal
    def cobrar_tarifa(self):
        super().sacar(self.__tarifa_mensal)
    def exibir_dados(self):
        return f'{super().exibir_dados()}'