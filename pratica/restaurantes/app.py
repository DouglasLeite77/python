from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.pratos import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
suco = Bebida('Suco', 5,'x', 'x', 'Grande')
arroz = Prato('Arroz', 5, 'Simples arroz','x')
tuta = Sobremesa('tuta', 2, 'x', 'x', 'tutinha')
suco.aplicar_desconto()
arroz.aplicar_desconto()
restaurante_praca.adiciona_no_cardapio(suco)
restaurante_praca.adiciona_no_cardapio(arroz)
restaurante_praca.adiciona_no_cardapio(tuta)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()