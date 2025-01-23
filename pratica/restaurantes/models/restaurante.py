from models.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliação = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurentes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurentes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}') 
    
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliação.append(avaliacao)
    
    @property
    def media_avaliacao(self):
        if not self._avaliação:
            return 'Sem avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliação)
        quantidade_notas = len(self._avaliação)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media