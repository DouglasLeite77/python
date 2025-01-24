from abc import ABC, abstractmethod

class Item_cardapio(ABC):

    def __init__(self, nome, preco, categoria, descricao):
        self._nome = nome
        self._preco = preco
        self._categoria = categoria
        self._descricao = descricao

    @abstractmethod
    def aplicar_desconto(self):
        pass

    