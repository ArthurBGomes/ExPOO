from endereco import Endereco

class Cliente:
    def __init__(self,nome,cpf,rua,numero,bairro,cidade):
        self.__nome = nome
        self.__cpf = cpf 
        self.__endereco = Endereco(rua,numero,bairro,cidade)
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

    
    