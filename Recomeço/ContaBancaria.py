class ContaBancaria:
    numeros_contas = []
    contas_duplicada = []
    def __init__(self,cliente,numero,saldo):
        self.__cliente = cliente 
        self.__numero =  numero
        self.__saldo = saldo
        ContaBancaria.numeros_contas.append(self.__numero)
    @classmethod
    def existe_conta_duplicada(cls):
        return len(cls.numeros_contas) != len(set(cls.numeros_contas))
    @classmethod
    def contas_duplicadas(cls):
        vistos = set()
        for numero in cls.numeros_contas:
            if numero in vistos:
                cls.contas_duplicada.append(numero)
            else:
                vistos.add(numero)
        return cls.contas_duplicada
    def get_cliente(self):
        return self.__cliente
    
    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo
    
    def depositar(self,valor):
        self.__saldo += valor
        return True
    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False
    def transferir(self,valor,destino):
            if self.sacar(valor):
                destino.depositar(valor)
                return True
            else:
                return False


    def exibir_dados(self):
        return f"{self.get_cliente()}, Conta {self.get_numero()}, possui {self.get_saldo():.2f} Reais disponíveis na conta"