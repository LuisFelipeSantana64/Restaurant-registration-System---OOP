from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco ):
        self.__nome = nome
        self.__preco = preco
    
    @property #getter preço
    def preco(self):
        return self.__preco

    @property #getter preço
    def nome(self): 
        return self.__nome

    @preco.setter #setter preço
    def preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self.__preco = novo_preco
        else:
            raise ValueError("O preço deve ser um número positivo.")
        
    @nome.setter #setter nome
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @abstractmethod
    def aplicar_desconto(self): #deve ter esse metodo na classe filha
        pass