class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.estado_ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'\n{self.nome} | {self.categoria} | {self.estado_ativo}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.estado_ativo}')

restaurante1 = Restaurante('Praça', 'Gourmet')

Restaurante.listar_restaurantes()
print(restaurante1)