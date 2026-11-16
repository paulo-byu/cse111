from endereco import extrair_cidade, extrair_estado, extrair_cep
import pytest

def test_extrair_cidade():
    assert extrair_cidade("Rua das Flores, 123, Centro, Curitiba - PR, 80000-000") == "Curitiba"
    assert extrair_cidade("Avenida Paulista, 1000, Bela Vista, São Paulo - SP, 01310-100") == "São Paulo"
    assert extrair_cidade("Avenida Centenário, 2200, Mangueirão, Belém - PA, 66640-658") == "Belém"

def test_extrair_estado():
    assert extrair_estado("Rua das Flores, 123, Centro, Curitiba - PR, 80000-000") == "PR"
    assert extrair_estado("Avenida Paulista, 1000, Bela Vista, São Paulo - SP, 01310-100") == "SP"
    assert extrair_estado("Avenida Centenário, 2200, Mangueirão, Belém - PA, 66640-658") == "PA"

def test_extrair_cep():
    assert extrair_cep("Rua das Flores, 123, Centro, Curitiba - PR, 80000-000") == "80000-000"
    assert extrair_cep("Avenida Paulista, 1000, Bela Vista, São Paulo - SP, 01310-100") == "01310-100"
    assert extrair_cep("Avenida Centenário, 2200, Mangueirão, Belém - PA, 66640-658") == "66640-658"




pytest.main(["-v", "--tb=line", "-rN", __file__])