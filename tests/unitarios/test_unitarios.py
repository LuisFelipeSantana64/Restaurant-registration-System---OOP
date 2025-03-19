import pytest
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

@pytest.fixture
def prato():
    return Prato("potato", 40.0, "simple potatos")

@pytest.fixture
def bebida():
    return Bebida("water", 15.0, "500ml")

@pytest.fixture
def restaurante():
    return Restaurante("SquareWhite", "Pub")


def test_criar_restaurante():
    restaurant1 = Restaurante("teste", "teste")
    assert isinstance(restaurant1, Restaurante)

    with pytest.raises(AttributeError):
        restaurant1 = Restaurante(1, "teste")

    with pytest.raises(AttributeError):
        restaurant1 = Restaurante("teste", 1)

    with pytest.raises(AttributeError): 
        restaurant1 = Restaurante(1,1)   



