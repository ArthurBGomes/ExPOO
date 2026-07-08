from ContaBancaria import ContaBancaria

class ContaSalario(ContaBancaria):
    def __init__(self, cliente, numero, saldo,empresa,saques_realizados):
        super().__init__(cliente, numero, saldo)
        self.__empresa = empresa
        self.__saques_realizados = saques_realizados

    def get_tipo_conta(self):
        return "Conta Salário"