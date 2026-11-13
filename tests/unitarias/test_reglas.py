import pytest
from apartalo.reglas import calcular_total_renta, calcular_cancelacion

@pytest.mark.unitaria
def test_renta_base_antes_18():
    assert calcular_total_renta(hora_inicio=15, es_fin_de_semana=False, arbitro=False) == 800.0

@pytest.mark.unitaria
def test_renta_base_despues_18():
    assert calcular_total_renta(hora_inicio=19, es_fin_de_semana=False, arbitro=False) == 1050.0

@pytest.mark.unitaria
def test_renta_fin_de_semana_y_arbitro():
    assert calcular_total_renta(hora_inicio=10, es_fin_de_semana=True, arbitro=True) == 1170.0

@pytest.mark.unitaria
def test_excepcion_hora_invalida():
    with pytest.raises(ValueError):
        calcular_total_renta(hora_inicio=25, es_fin_de_semana=False, arbitro=False)

@pytest.mark.unitaria
@pytest.mark.parametrize(
    "total_pagado, horas, reembolso_esperado",
    [
        (1000.0, 30.0, 1000.0),
        (1000.0, 24.0, 1000.0),
        (1000.0, 12.0, 500.0),
        (1000.0, 6.0, 500.0),
        (1000.0, 4.0, 0.0),
        (1000.0, 0.0, 0.0),
    ]
)
def test_cancelacion_parametrizada(total_pagado, horas, reembolso_esperado):
    assert calcular_cancelacion(total_pagado, horas) == reembolso_esperado

@pytest.mark.unitaria
def test_excepcion_cancelacion_negativa():
    with pytest.raises(ValueError):
        calcular_cancelacion(-500.0, 10.0)

