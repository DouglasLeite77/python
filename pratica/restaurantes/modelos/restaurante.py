from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import Item_cardapio

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} |{restaurante.ativo}') 
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adiciona_no_cardapio(self,item):
        if isinstance(item,Item_cardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        for i,item in enumerate(self._cardapio,start=1):
            if  hasattr(item,'_tamanho'):
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)
            elif hasattr(item, '_tipo'):
                mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Tipo: {item._tipo}'
                print(mensagem_sobremesa) 
            else:
                mensagem = f'{i}. Nome:{item._nome} | Preço: {item._preco} | Descrição: {item._descricao}'
                print(mensagem)

