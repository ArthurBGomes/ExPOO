class Endereco:
    def __init__(self,rua,numero,bairro,cidade):
        self.__rua:str = rua
        self.__numero:int = numero
        self.__bairro:str = bairro
        self.__cidade:str = cidade

    def get_rua(self):
        return self.__rua
    def get_numero(self):
        return self.__numero
    def get_bairro(self):
        return self.__bairro
    def get_cidade(self):
        return self.__cidade
    def exibir_dados(self):
        return (f"Rua: {self.__rua}\n"
                f"Número: {self.__numero}\n"
                f"Bairro: {self.__bairro}\n"
                f"Cidade: {self.__cidade}"             
    )
class Cliente:
    def __init__(self,nome,cpf,endereco):
        self.__nome = nome
        self.__cpf = cpf 
        self.__endereco = endereco
        self.__contas = []
    def get_nome(self):
        return self.__nome 
    def get_cpf(self):
        return self.__cpf
    def get_endereco(self):
        return self.__endereco
    def exibir_dados(self):
        return (f"=== CLIENTE ===\n"
                f"Nome: {self.__nome}\n"
                f"CPF: {self.__cpf}\n"
                f"{self.__endereco.exibir_dados()}")
    def adicionar_conta(self,conta):
        self.__contas.append(conta) 
    def possui_conta(self):
        return len(self.__contas) > 0
        
    def buscar_conta(self,numero):
        for n in self.__contas:
            if n.get_numero() == numero:
                return f"{n.get_titular().get_nome()} tem a conta {n.get_numero()}"
        return None
    def consultar_saldo_total(self):
        saldo_total = 0 
        for n in self.__contas:
            saldo_total += n.get_saldo()
        return saldo_total
    def quantidade_contas(self):
        if len(self.__contas) >=1:
            return len(self.__contas)
        else:
            return len(self.__contas)
class ContaBancaria:
    numeros_contas = []
    contas_duplicada = []
    def __init__(self,cliente,numero,saldo):
        self.__cliente = cliente 
        self.__numero =  numero
        self.__saldo = saldo
        self.__ativa = True
        ContaBancaria.numeros_contas.append(self.__numero)
        cliente.adicionar_conta(self) # adicionar essa linha pro método consultar_saldo_total funcionar

    def get_ativa(self):
        return self.__ativa
    def bloquear_conta(self):
        self.__ativa = False
    def desbloquear_conta(self):
        self.__ativa = True
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
    def get_titular(self):
        return self.__cliente.get_nome()
    
    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,valor):
        self.__saldo = valor 
        
    
    def get_tipo_conta(self):
        return "Conta Bancária"
    def depositar(self,valor):
        self.__saldo += valor
        return True
    def sacar(self,valor):
        if self.__ativa:
            if self.__saldo >= valor:
                self.__saldo -= valor
                return True
            else:
                return False
        else:
            return False
    def transferir(self,valor,destino):
            if self.sacar(valor):
                destino.depositar(valor)
                return True
            else:
                return False


    def exibir_dados(self):
        return (f"{self.__cliente.exibir_dados()}\n"
                f"=== CONTA ===\n"
                f"Número: {self.get_numero()}\n"
                f"Saldo: {self.get_saldo():.2f}R$")
    def pix(self,valor, conta_destino):
        return self.transferir(valor, conta_destino)
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
        return self.sacar(self.__tarifa_mensal) #colocar o return aqui
    def get_tipo_conta(self):
        return "Conta Corrente"
    def exibir_dados(self) -> str:
        return f'{super().exibir_dados()}\nLimite:{self.__limite:.2f}R$\nTarifa:{self.__tarifa_mensal:.2f}R$'
class ContaPoupanca(ContaBancaria):
    def __init__(self, cliente, numero, saldo,taxa_rendimento):
        super().__init__(cliente, numero, saldo)
        self.__taxa_rendimento = taxa_rendimento
    def sacar(self, valor):
        return False
    def get_tipo_conta(self):
        return 'Conta Poupança'
    def render_juros(self):
        self.set_saldo(self.get_saldo() + self.__taxa_rendimento * self.get_saldo())
        return None
    def exibir_dados(self):
         return f"{super().exibir_dados()}\nTaxa:{self.__taxa_rendimento}"
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