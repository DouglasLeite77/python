from modelos.cardapio.item_cardapio import Item_cardapio

class Sobremesa(Item_cardapio):
    
    def __init__(self, nome, preco, categoria, descricao, tipo):
        super().__init__(nome, preco, categoria, descricao)
        self._tipo = tipo  

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        pass