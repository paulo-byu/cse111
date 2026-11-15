"""Verifique se as funções prefixo e sufixo funcionam corretamente."""

from palavras import prefixo, sufixo
import pytest


def test_prefixo():
    """Verifique se a função prefixo funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """
    assert prefixo("", "") == ""
    assert prefixo("", "correto") == ""
    assert prefixo("imparcial", "") == ""
    assert prefixo("autoescola", "marinha") == ""
    assert prefixo("submarino", "subproduto") == "sub"
    assert prefixo("intermunicipal", "interestadual") == "inter"
    assert prefixo("antissocial", "alento") == "a"
    assert prefixo("supermercado", "superlotado") == "super"
    assert prefixo("hipermercado", "hipertexto") == "hiper"

def test_sufixo():
    """Verifique se a função sufixo funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """
    assert sufixo("", "") == ""
    assert sufixo("", "correto") == ""
    assert sufixo("imparcial", "") == ""
    assert sufixo("prever", "") == ""
    assert sufixo("cansado", "fatigado") == "ado"
    assert sufixo("nadando", "voando") == "ando"
    assert sufixo("trator", "redutor") == "tor"
    assert sufixo("animal", "pedestal") == "al"
    assert sufixo("respeitoso", "precioso") == "oso"

pytest.main(["-v", "--tb=line", "-rN", __file__])