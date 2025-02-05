from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante1.avaliar_restaurante('Felipe', 9)
restaurante1.avaliar_restaurante('Igor', 4)
bebida1 = Bebida('Suco de Melancia', 5.0,'grande')
prato1 = Prato('Paozinho',2.00,'O melhor pão da cidade')


def main():
    Restaurante.listar_restaurantes()
    print(f"\033[1;34m \n\tALTERANDO STATUS\033[0m")
    restaurante1.alterar_estado()
    Restaurante.listar_restaurantes()
    print(restaurante1.categoria) #usando getter
    print(restaurante1.nome) #usando getter
    print(f"\033[1;34m \n\tALTERANDO STATUS\033[0m")
    restaurante1.alterar_estado()
    Restaurante.listar_restaurantes()
    print(restaurante1) #usando __str__
    print(prato1) #usando __str__
    print(bebida1) #usando __str__

if __name__ == '__main__':
    main()