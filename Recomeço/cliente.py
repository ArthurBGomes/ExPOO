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
        return f"{self.__nome},{self.__cpf},{self.__endereco.exibir_dados()}"
    def adicionar_conta(self,conta):
        self.__contas.append(conta)

    
    