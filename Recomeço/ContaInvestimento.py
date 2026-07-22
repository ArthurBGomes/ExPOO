from Recomeço.ContaBancária import ContaBancaria

class ContaInvestimento(ContaBancaria):
    def __init__(self, cliente, numero, saldo,taxa_rendimento,taxa_administracao):
        super().__init__(cliente, numero, saldo)
        self.__taxa_rendimento = taxa_rendimento 
        self.__taxa_administracao = taxa_administracao
    def sacar(self, valor):
        return False
    def get_tipo_conta(self):
        return 'Conta Investimento'
    def render_juros(self):
        self.set_saldo(self.get_saldo() + self.__taxa_rendimento * self.get_saldo())
        self.set_saldo(self.get_saldo() - self.__taxa_administracao)
        return None
    def exibir_dados(self):
         return f"{super().exibir_dados()}\nTaxa:{self.__taxa_rendimento}"