from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, cliente, numero, saldo,taxa_rendimento):
        super().__init__(cliente, numero, saldo)
        self.__taxa_rendimento = taxa_rendimento
    def get_tipo_conta(self):
        pass
    def render_juros(self):
        pass
    def exibir_dados(self):
        f"{super().exibir_dados()}"