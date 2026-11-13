"""Pruebas para los Requisitos No Funcionales (RNF) del sistema."""

import pytest
from apartalo.reglas import calcular_total_renta


@pytest.mark.rnf
def test_rnf_robustez_entradas_invalidas():
    """Comprueba el requisito no funcional de robustez ante entradas erróneas."""
    with pytest.raises(ValueError):
        calcular_total_renta(hora_inicio=25, es_fin_de_semana=False, arbitro=False)

    with pytest.raises(ValueError):
        calcular_total_renta(hora_inicio=-2, es_fin_de_semana=True, arbitro=True)

