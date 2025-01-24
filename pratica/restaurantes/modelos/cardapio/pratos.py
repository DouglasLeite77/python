from modelos.cardapio.item_cardapio import Item_cardapio

class Prato(Item_cardapio):

    def __init__(self, nome, preco, categoria, descricao):
        super().__init__(nome, preco, categoria, descricao)

    def __str__(self):
        return self._nome