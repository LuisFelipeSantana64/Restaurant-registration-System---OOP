from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #herdando
    def __init__ (self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.__descricao = descricao

    def __str__(self):
        return self.nome #acesso por meio do getter da classe pai
    
    @property
    def descricao(self):
        return self.__descricao
    
    def aplicar_desconto(self):
        self.preco = self.preco - (self.preco * 0.05)