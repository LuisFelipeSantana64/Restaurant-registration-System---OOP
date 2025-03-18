import pytest
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def test_fluxo_completo(capfd, mocker):
    restaurante1 = Restaurante("Gourmet Place", "Italiana")
    restaurante1.alterar_estado()
    bebida = Bebida("Vinho Tinto", 50.0, "750ml")
    prato = Prato("Risoto", 30.0, "Risoto de cogumelos")
    
    restaurante1.adicionar_no_cardapio(bebida)
    restaurante1.adicionar_no_cardapio(prato)
    
    bebida.aplicar_desconto()
    prato.aplicar_desconto()
    
    restaurante1.avaliar_restaurante("João", 5)
    restaurante1.avaliar_restaurante("Ana", 3)
    
    assert restaurante1.media_avaliacao == 4.0
    restaurante1.exibir_cardapio
    # Captura a saída do print
    captured = capfd.readouterr()

    # Verifica se os itens aparecem corretamente na saída do print
    assert "Vinho Tinto" in captured.out
    assert "45.0" in captured.out
    assert "Risoto" in captured.out
    assert "28.5" in captured.out
    
    with pytest.raises(TypeError):
        restaurante1.adicionar_no_cardapio("Não é um item válido")
    
    with pytest.raises(ValueError):
        restaurante1.avaliar_restaurante("Pedro", -6)

    mocker.patch("builtins.input", return_value="1")
    restaurante1.alterar_estado()
    assert restaurante1.ativo == "☐"