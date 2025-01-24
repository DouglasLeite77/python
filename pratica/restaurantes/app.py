from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.pratos import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
suco = Bebida('Suco', 5,'x', 'x', 'Grande')
arroz = Prato('Arroz', 5, 'Simples arroz','x')
restaurante_praca.adiciona_no_cardapio(suco)
restaurante_praca.adiciona_no_cardapio(arroz)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()