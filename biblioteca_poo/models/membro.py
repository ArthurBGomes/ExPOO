from models.pessoa import Pessoa


class Membro(Pessoa):

    def __init__(self, nome, endereco, id_membro, contato, data_cadastro):
        super().__init__(nome, endereco)

        self._id_membro = None
        self.id_membro = id_membro

        self.contato = contato
        self.data_cadastro = data_cadastro

    @property
    def id_membro(self):
        return self._id_membro

    @id_membro.setter
    def id_membro(self, valor):
        if valor < 0:
            print("Erro: id_membro não pode ser negativo.")
        else:
            self._id_membro = valor

    def __str__(self):
        return f"Membro: {self.nome} | ID: {self.id_membro}"
