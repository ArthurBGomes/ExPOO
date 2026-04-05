class ItemPedido:
    def __init__(self,produto,quantidade,preco):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
class Pedido:
    def __init__(self):
        self.items = []
    def adicionar_item(self,produto,quantidade,preco):
        item = ItemPedido(produto,quantidade,preco)
        self.items.append(item)
    def calcular_total(self):
        produtos =  0
        preco_total = 0
        for produto in self.items:
            produtos += produto.quantidade
            preco_total += produto.preco
        print(f"a Compra de {produtos} produtos custou um total de {preco_total:.2f}R$,Volte sempre!!")

pedido = Pedido()
pedido.adicionar_item("Teclado Gamer",1,120)
pedido.adicionar_item("Mousepad Gamer",1,80)
pedido.adicionar_item("Monitor",1,160)
pedido.calcular_total()