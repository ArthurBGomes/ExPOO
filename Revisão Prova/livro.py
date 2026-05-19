from itembiblioteca import ItemBiblioteca
class Livro(ItemBiblioteca):
    def __init__(self,titulo,autor,isbn):
        self.titulo:str = titulo
        self.autor:str = autor
        self.isbn:int = isbn
    def exibir_detalhes(self):
        return (
            f"Título: {self.titulo} | "
            f"Autor: {self.autor} | "
            f"ISBN: {self.isbn} | "
        )
    def get_identificador(self):
        return f"ISBN: {self.isbn}"

# O Init serve pra declarar os parâmetros necessários quando vamos instanciar um objeto
# o self é necessário pois é ele que se refere ao objeto,e obrigatório em todas as partes
# self é uma referência ao próprio objeto que está sendo criado ou manipulado. É o primeiro parâmetro de todo método de instância, e através dele cada objeto acessa seus próprios atributos e métodos — sem confundir com os de outros objetos da mesma classe.
# O __init__ é o construtor da classe — um método especial chamado automaticamente toda vez que um novo objeto é criado. Sua função é inicializar os atributos do objeto, ou seja, definir o estado inicial da instância.