from Recomeço.ContaBancária import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, cliente, numero, saldo,limite,tarifa_mensal,limite_por_saque,nome_pacote):
        super().__init__(cliente, numero, saldo)
        self.__limite:float = limite
        self.__tarifa_mensal:float = tarifa_mensal
        self.__limite_por_saque:float = limite_por_saque
        self.nome_pacote:str = nome_pacote
    def get_limite_por_saque(self) -> float:
        return self.__limite_por_saque

    def sacar(self, valor: float) -> bool:
        if not self.get_ativa():
            return False
        if valor <= 0 or valor > self.__limite_por_saque:
            return False
        if valor <= self.get_saldo():
            return super().sacar(valor)
        elif valor <= self.get_saldo() + self.__limite:
            self.set_saldo(self.get_saldo() - valor)
            return True
        else:
            return False
    def cobrar_taxa(self) -> None:
        return self.sacar(self.__tarifa_mensal) 
    def get_tipo_conta(self):
        return "Conta Corrente"
    def exibir_dados(self) -> str:
        return f'{super().exibir_dados()}\nLimite:{self.__limite:.2f}R$\nTarifa:{self.__tarifa_mensal:.2f}R$'
    