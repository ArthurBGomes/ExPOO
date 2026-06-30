from ContaBancaria import ContaBancaria

class ContaSalario(ContaBancaria):
    def __init__(self, cliente, numero, saldo,limite,tarifa_mensal):
        super().__init__(cliente, numero, saldo)
        self.__limite = limite
        self.__tarifa_mensal = tarifa_mensal