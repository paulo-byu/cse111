from nomes import criar_nome_completo, extrair_sobrenome, extrair_primeiro_nome
import pytest
def test_criar_nome_completo():
    assert criar_nome_completo("Alexandre", "Nascimento") == "Nascimento; Alexandre"
    assert criar_nome_completo("Ana", "Sá") == "Sá; Ana"
    assert criar_nome_completo("Ava", "Lopes-João") == "Lopes-João; Ava"

def test_extrair_sobrenome():
    assert extrair_sobrenome("Nascimento; Alexandre") == "Nascimento"
    assert extrair_sobrenome("Sá; Ana") == "Sá"
    assert extrair_sobrenome("Lopes-João; Ava") == "Lopes-João"

def test_extrair_primeiro_nome():
    assert extrair_primeiro_nome("Nascimento; Alexandre") == "Alexandre"
    assert extrair_primeiro_nome("Sá; Ana") == "Ana"
    assert extrair_primeiro_nome("Lopes-João; Ava") == "Ava"





pytest.main(["-v", "--tb=line", "-rN", __file__])