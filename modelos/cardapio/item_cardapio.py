from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco ):
        self.__nome = nome
        self.__preco = preco
    
    @property #getter preço
    def preco(self):
        return self.__preco

    @property #getter nome
    def nome(self): 
        return self.__nome

    @preco.setter #setter preço
    def preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self.__preco = novo_preco
        if isinstance(novo_preco, str):
            raise TypeError("O preço deve ser um numero.")
        if novo_preco < 0 :
            raise ValueError("O preço deve ser positivo")
        
    @nome.setter #setter nome
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    @abstractmethod
    def aplicar_desconto(self): #deve ter esse metodo na classe filha
        pass