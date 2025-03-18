import pytest
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# Fixtures para criar instâncias de Prato e Bebida
@pytest.fixture
def prato():
    return Prato("Feijoada", 40.0, "Feijoada tradicional")

@pytest.fixture
def bebida():
    return Bebida("Suco de Laranja", 15.0, "500ml")


def test_criar_prato(prato):
    """Teste para verificar a criação de um Prato"""
    assert prato.nome == "Feijoada"
    assert prato.preco == 40.0
    assert prato.descricao == "Feijoada tradicional"


def test_criar_bebida(bebida):
    """Teste para verificar a criação de uma Bebida"""
    assert bebida.nome == "Suco de Laranja"
    assert bebida.preco == 15.0
    assert bebida.tamanho == "500ml"


def test_getter_setter_prato(prato):
    """Teste para os getters e setters da classe Prato"""
    # Testando getter de nome
    assert prato.nome == "Feijoada"
    
    # Testando setter de nome
    prato.nome = "Arroz com Feijão"
    assert prato.nome == "Arroz com Feijão"
    
    # Testando getter de preco
    assert prato.preco == 40.0
    
    # Testando setter de preco
    prato.preco = 45.0
    assert prato.preco == 45.0
    
    # Testando setter de preco com valor inválido (deve lançar ValueError)
    with pytest.raises(ValueError):
        prato.preco = -10


def test_getter_setter_bebida(bebida):
    """Teste para os getters e setters da classe Bebida"""
    # Testando getter de nome
    assert bebida.nome == "Suco de Laranja"
    
    # Testando setter de nome
    bebida.nome = "Suco de Manga"
    assert bebida.nome == "Suco de Manga"
    
    # Testando getter de preco
    assert bebida.preco == 15.0
    
    # Testando setter de preco
    bebida.preco = 18.0
    assert bebida.preco == 18.0
    
    # Testando setter de preco com valor inválido (deve lançar ValueError)
    with pytest.raises(ValueError):
        bebida.preco = -5


def test_aplicar_desconto_prato(prato):
    """Teste de integração para o método aplicar_desconto na classe Prato"""
    prato.aplicar_desconto() 
    assert prato.preco == 38.0


def test_aplicar_desconto_bebida(bebida):
    """Teste de integração para o método aplicar_desconto na classe Bebida"""
    bebida.aplicar_desconto()
    assert bebida.preco == 13.50
