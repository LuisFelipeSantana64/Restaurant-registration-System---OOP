from modelos.restaurante import Restaurante

restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante1.avaliar_restaurante('Felipe', 9)
restaurante1.avaliar_restaurante('Igor', 4)
restaurante1.avaliar_restaurante('Joao', 1)


def main():
    Restaurante.listar_restaurantes()
    restaurante1.alterar_estado()
    Restaurante.listar_restaurantes()
    print(restaurante1.categoria) #usando getter
    print(restaurante1.nome) #usando getter
    restaurante1.alterar_estado()
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()