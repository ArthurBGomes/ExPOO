class ContaBancaria:
    def __init__(self,titular):
        self.titular = titular
        self.__saldo = 0
    @property
    def get_saldo(self,):
        return self.__saldo
    @get_saldo.setter
    def set_saldo(self,valor):
        if valor > 0:
            self.__saldo =  valor
        else:
            print("Coloque um valor positivo")
    def depositar(self,valor):
        if valor <= 0:
            print("Valor de depósito Inválido")
        else:
            self.__saldo += valor
    def sacar(self,valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo Inválido ou insuficiente")
    def consultar_saldo(self):
        return self.__saldo
c1 = ContaBancaria("Arthur",)
c1.depositar(500)
c1.sacar(200)
print(f"Saldo atual: {c1.consultar_saldo()}")
c1.set_saldo = 1000
print(c1.get_saldo)
