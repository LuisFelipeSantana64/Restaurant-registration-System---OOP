class Restaurantes:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.estado_ativo = False

    def __str__(this):
        return f'\n{this.nome} | {this.categoria}'

restaurante1 = Restaurantes('Praça', 'Gourmet')

print(restaurante1)
