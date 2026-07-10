from ContaBancaria import ContaBancaria

class ContaSalario(ContaBancaria):
    def __init__(self, cliente, numero, saldo,empresa,saques_realizados,limite_saques):
        super().__init__(cliente, numero, saldo)
        self.__empresa = empresa
        self.__saques_realizados = saques_realizados
        self.__limite_saques = limite_saques

    def receber_salario(self, valor):
        super().depositar(valor)

    def sacar(self, valor):
        self.__saques_realizados += 1
        if (self.__saques_realizados > self.__limite_saques) :
            return 'Limite de saques atingido!'
        else:
            return super().sacar(valor)
    
    def depositar(self, valor):
        return False
    
    def transferir(self, valor, destino):
        return False
    
    def exibir_dados(self):
        return f"{super().exibir_dados()}\nEmpresa:{self.__empresa}\nLimite de Saque:{self.__limite_saques}"
    
    def get_tipo_conta(self):
        return "Conta Salário"