import pytest
from apartalo.reglas import calcular_total_renta, calcular_cancelacion

@pytest.mark.aceptacion
@pytest.mark.parametrize(
    "hora_inicio, es_fin_de_semana, arbitro, esperado",
    [
        (10, False, False, 800.0),
        (19, False, False, 1050.0),
        (10, True, False, 920.0),
        (19, True, False, 1207.5),
        (14, False, True, 1050.0),
    ]
)
def test_aceptacion_renta_cancha(hora_inicio, es_fin_de_semana, arbitro, esperado):
    # Dado los parámetros de reserva de cancha y horario
    # Cuando se calcula el costo total de la renta
    resultado = calcular_total_renta(hora_inicio, es_fin_de_semana, arbitro)
    # Entonces el total coincide con las tarifas oficiales de la variante
    assert resultado == esperado


@pytest.mark.aceptacion
@pytest.mark.parametrize(
    "total_pagado, horas_anticipacion, reembolso_esperado",
    [
        (1000.0, 30.0, 1000.0),
        (1000.0, 24.0, 1000.0),  # Límite exacto de 24 horas
        (1000.0, 12.0, 500.0),
        (1000.0, 6.0, 500.0),   # Límite exacto de 6 horas
        (1000.0, 4.0, 0.0),
        (1000.0, 1.0, 0.0),
    ]
)
def test_aceptacion_cancelacion(total_pagado, horas_anticipacion, reembolso_esperado):
    # Dado un monto pagado y las horas de anticipación para cancelar
    # Cuando se procesa el reembolso
    resultado = calcular_cancelacion(total_pagado, horas_anticipacion)
    # Entonces el porcentaje devuelto cumple con las reglas de negocio
    assert resultado == reembolso_esperado
