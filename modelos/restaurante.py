class Restaurante:
    restaurantes = []
 
    def __init__(self, nome, categoria):
        self.__nome = nome.title()
        self.__categoria = categoria.title()
        self.__ativo = False
        Restaurante.restaurantes.append(self)
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'NOME RESTAURANTE'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'ATIVADO'.ljust(25) }\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.__nome.ljust(25)} | {restaurante.__categoria.ljust(25)} | {restaurante.ativo}')

    def __str__(self):
        return f'\n{self.__nome} | {self.__categoria} | {self.ativo}'
    
    def alterar_estado(self):
        print(f"\033[1;34m \n\tALTERANDO ESTADO\033[0m")
        if self.__ativo == False:
            self.__ativo = not self.__ativo
            print(f"O restaurante'\033[92m{self.__nome}\033[0m'foi ativado com sucesso!!")
        else:
            try:
                decisao = int(input(f"'{self.__nome}' já está ativado, deseja desativar? (1 para sim):"))
                if decisao == 1:
                    self.__ativo = not self.__ativo
                    print(f"\nO restaurante '{self.__nome}' foi desativado com sucesso!!")
                else:
                    print("\nNão houve mudança!!")
            except: 
                print("\nNão houve mudança!")

        
    @property #getter
    def ativo(self): 
        return '☑'if self.__ativo else '☐' 

restaurante1 = Restaurante('Praça', 'Gourmet')

Restaurante.listar_restaurantes()
restaurante1.alterar_estado()
Restaurante.listar_restaurantes()



