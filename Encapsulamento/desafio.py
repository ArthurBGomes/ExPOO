class Produto:
    def __init__(self,nome,preco,quantidade):
        self.__nome:str = nome
        self.__preco:float = preco
        self.__quantidade_em_estoque:int = quantidade
    
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self,valor):
        if valor <= 0:
            print("Valor Invalido")
        else:
            self.__preco = valor
    @property
    def quantidade_em_estoque(self):
        return self.__quantidade_em_estoque
    @quantidade_em_estoque.setter
    def quantidade_em_estoque(self,valor):
        if valor <= 0:
            print("valor invalido")
        else:
            self.quantidade_em_estoque = valor
            
    def vender(self,quantidade):
        if 0 < self.__quantidade_em_estoque >= quantidade:
            self.__quantidade_em_estoque -= quantidade
        else:
            print("Não tem estoque suficiente")
    def repor_estoque(self,quantidade):
        self.__quantidade_em_estoque += quantidade
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_quantidade_em_estoque(self):
        return self.__quantidade_em_estoque
p1 = Produto("Celular",2500,2)
print(f"Produto: {p1.get_nome()}, Preço: R${p1.get_preco():.2f}, Estoque: {p1.get_quantidade_em_estoque()}")
p1.repor_estoque(5)
p1.vender(3)
print(f"Estoque atual: {p1.get_quantidade_em_estoque()}")
p1.vender(15) # Tentativa de vender mais do que há em estoque
