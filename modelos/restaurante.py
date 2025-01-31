from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
 
    def __init__(self, nome, categoria):
        self.__nome = nome.title()
        self.__categoria = categoria.title()
        self.__avaliacao = []
        self.__ativo = False
        Restaurante.restaurantes.append(self)
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'NOME RESTAURANTE'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'AVALIAÇÃO'.ljust(25)} | {'ATIVADO'.ljust(25) }\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.__nome.ljust(25)} | {restaurante.__categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}') #posso acessar com '__' porque está dentro da classe

    def __str__(self):
        return f'\n{self.__nome} | {self.__categoria} | {self.ativo}' #posso acessar com '__' porque está dentro da classe

        
    @property #getter ativo
    def ativo(self): 
        return '☑'if self.__ativo else '☐' 
    
    @property #getter categoria
    def categoria(self):
        return self.__categoria

    @property #getter nome
    def nome(self):
        return self.__nome

    
    def alterar_estado(self):
        print(f"\033[1;34m \n\tALTERANDO STATUS\033[0m")
        if self.__ativo == False:
            self.__ativo = not self.__ativo
            print(f"O restaurante'\033[92m{self.__nome}\033[0m'foi ativado com sucesso!!\n")
        else:
            try:
                decisao = int(input(f"'{self.__nome}' já está ativado, deseja desativar? (1 para SIM):"))
                if decisao == 1:
                    self.__ativo = not self.__ativo
                    print(f"\nO restaurante '{self.__nome}' foi desativado com sucesso!!\n")
                else:
                    print("\nNão houve mudança!!")
            except: 
                print("\nNão houve mudança!!")
    
    def avaliar_restaurante(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self.__avaliacao.append(avaliacao)
        
    @property
    def media_avaliacao(self):
        if not self.__avaliacao:
            return 0
        soma = sum(avaliacao.nota for avaliacao in self.__avaliacao)
        return round(soma / (len(self.__avaliacao)), 1)
        


