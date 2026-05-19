from pessoa import Pessoa
class Membro(Pessoa):
    def __init__(self,nome,endereco,id_membro,contato,data_cadastro):
        super().__init__(nome,endereco)
        self.id_membro:int = id_membro
        self.contato:str = contato
        self.data_cadastro = data_cadastro
    @property
    def id_membro(self): # getter
        return self.__id_membro
    @id_membro.setter 
    def id_membro(self,valor): # Mesmo nome do Getter
        if valor < 0:
            print('O valor não pode ser negativo')
        else:
            self.__id_membro = valor
    def __str__(self):
        return f"Nome: {self.nome} e id: {self.__id_membro}"
# m1 = Membro("Arthur",1211,"email@gmail.com")

# print(m1)
# m1.id_membro = -5 # bloqueado e não muda nada
# print(m1.id_membro) # continua sendo o valor inicial