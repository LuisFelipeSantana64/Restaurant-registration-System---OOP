from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio): #herdando
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.__tamanho = tamanho

    def __str__(self):
        return self.nome #acesso por meio do getter da classe pai
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    def aplicar_desconto(self):
        self.preco = self.preco - (self.preco * 0.10)
