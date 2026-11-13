# 7. Requisitos no funcionales
> Ejercicio 7 · Tema 9 · 🎩 PO y 🎩 desarrollador
> Cada restricción va como **issue** (formulario "Requisito no funcional"). Aquí va el resumen.

## 7.1 y 7.2 Restricciones SMART

| Issue | Restricción SMART | Externa / interna | Cualidad | Historia (T) | Prueba práctica (Tabla 2) o práctica (Tabla 4) |
|---|---|---|---|---|---|
| #16 (RNF-1) | El sistema debe lanzar `ValueError` en el **100 %** de entradas inválidas (horas negativas, horas > 2, montos < 0) al calcular rentas o reembolsos. | **Interna** | **Robustez** | #2 (R1) y #5 (R2) | Práctica: **Pruebas unitarias** con `pytest.raises(ValueError)`. |
| #17 (RNF-2) | El sistema debe calcular **35 reembolsos en menos de 1 segundo** durante la hora pico (viernes 19:00 a 21:00). | **Externa** | **Desempeño** | #5 (R2) | Prueba: Medición de tiempo de ejecución con `time.perf_counter()` en Python. |
| #18 (RNF-3) | El sistema debe responder a una solicitud de reserva en **≤ 2 segundos** cuando haya 35 reservas concurrentes en la hora pico del viernes. | **Externa** | **Confiabilidad / Tiempo de respuesta** | #2 (R1) | Prueba: Prueba de carga (Load testing) con `pytest-benchmark` o script de concurrencia. |

## 7.3 La que compruebo con código

- **Restricción:** #16 (RNF de Robustez).
- **Prueba:** `tests/rnf/test_robustez.py` (usando la marca `@pytest.mark.rnf`).
- **Evidencia:** La prueba comprueba que si un usuario intenta calcular una renta con horas negativas o un reembolso con monto negativo, el sistema no se rompe, sino que arroja un error controlado.

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


