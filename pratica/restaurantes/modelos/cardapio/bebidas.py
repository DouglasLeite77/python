from modelos.cardapio.item_cardapio import Item_cardapio

class Bebida(Item_cardapio):

    def __init__(self, nome, preco, categoria, descricao, tamanho):
        super().__init__(nome, preco, categoria, descricao)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
        