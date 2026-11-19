from pytest import approx
import pytest
from fluxo_de_agua import calc_altura_coluna_agua, calc_pressao_pela_altura, calc_perda_pressao_tubo, calc_perda_pressao_conexoes, calc_num_reynolds, calc_perda_pressao_reducao_tubo, calc_kpa_para_mca


def test_calc_altura_coluna_agua():
    """Verifique se a função calc_altura_coluna_agua funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """
    assert calc_altura_coluna_agua(0.0, 0.0) == 0.0
    assert calc_altura_coluna_agua(0.0, 10.0) == 7.5
    assert calc_altura_coluna_agua(25.0, 0.0) == 25.0
    assert calc_altura_coluna_agua(48.3, 12.8) == 57.9

def test_calc_pressao_pela_altura():
    """Verifique se a função calc_pressao_pela_altura funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """
    assert calc_pressao_pela_altura(0.0) == approx(0.000, abs=0.001)
    assert calc_pressao_pela_altura(30.2) == approx(295.628, abs=0.001)
    assert calc_pressao_pela_altura(50.0) == approx(489.450, abs=0.001)

def test_calc_perda_pressao_tubo():
    """Verifique se a função calc_perda_pressao_tubo funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """    
    assert calc_perda_pressao_tubo(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert calc_perda_pressao_tubo(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert calc_perda_pressao_tubo(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

def test_calc_perda_pressao_conexoes():
    """Verifique se a função calc_perda_pressao_conexoes funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """
    assert calc_perda_pressao_conexoes(0.00, 3) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_conexoes(1.65, 0) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_conexoes(1.65, 2) == approx(-0.109, abs=0.001)
    assert calc_perda_pressao_conexoes(1.75, 2) == approx(-0.122, abs=0.001)
    assert calc_perda_pressao_conexoes(1.75, 5) == approx(-0.306, abs=0.001)

def test_calc_num_reynolds():
    """Verifique se a função calc_num_reynolds funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """
    assert calc_num_reynolds(0.048692, 0.00) == approx(0, abs=1)
    assert calc_num_reynolds(0.048692, 1.65) == approx(80069, abs=1)
    assert calc_num_reynolds(0.048692, 1.75) == approx(84922, abs=1)
    assert calc_num_reynolds(0.286870, 1.65) == approx(471729, abs=1)
    assert calc_num_reynolds(0.286870, 1.75) == approx(500318, abs=1)

def test_calc_perda_pressao_reducao_tubo():
    """Verifique se a função calc_perda_pressao_reducao_tubo funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """
    assert calc_perda_pressao_reducao_tubo(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_reducao_tubo(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert calc_perda_pressao_reducao_tubo(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

def test_calc_kpa_para_mca():
    """Verifique se a função calc_kpa_para_mca funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """
    assert calc_kpa_para_mca(0.000) == approx(0.000, abs=0.001)
    assert calc_kpa_para_mca(158.700) == approx(16.212, abs=0.001)
    assert calc_kpa_para_mca(-121.000) == approx(-12.360, abs=0.001)


# Chama a função main que faz parte do pytest para que o
# o computador execute as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])