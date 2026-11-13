"""Reglas de negocio de mi variante (Ejercicio 6).

Aquí van las funciones de R1 y R2. Escríbelas con TDD:
primero una prueba que falle (ROJO), luego el código mínimo para que pase (VERDE),
y después mejora el código sin romper las pruebas (REFACTOR).

Si una entrada no tiene sentido (horas negativas, un servicio que no existe, etc.),
la función debe lanzar ValueError.
"""

def calcular_total_renta(hora_inicio: int, es_fin_de_semana: bool, arbitro: bool) -> float:
    """
    R1: Total de la renta para Canchas de fútbol 7.
    - $800 antes de las 18:00; $1,050 a las 18:00 o después.
    - Sábado y domingo: 15% más sobre la renta.
    - Árbitro opcional: $250 sin recargo de fin de semana.
    """
    if not (0 <= hora_inicio <= 23):
        raise ValueError("La hora de inicio debe estar entre 0 y 23.")

    # Renta base según la hora
    if hora_inicio < 18:
        base = 800.0
    else:
        base = 1050.0

    # Recargo de fin de semana (15% solo sobre la renta base)
    if es_fin_de_semana:
        base *= 1.15

    total = base

    # Costo del árbitro (opcional, sin recargo)
    if arbitro:
        total += 250.0

    return round(total, 2)


def calcular_cancelacion(total_pagado: float, horas_anticipacion: float) -> float:
    """
    R2: Cancelación y reembolso para Canchas de fútbol 7.
    - Con 24 horas o más: se reembolsa el 100%.
    - Con 6 horas o más, pero menos de 24: se reembolsa el 50%.
    - Con menos de 6 horas: no se reembolsa ($0).
    """
    if total_pagado < 0:
        raise ValueError("El total pagado no puede ser negativo.")
    if horas_anticipacion < 0:
        raise ValueError("Las horas de anticipación no pueden ser negativas.")

    if horas_anticipacion >= 24:
        reembolso = total_pagado * 1.0
    elif horas_anticipacion >= 6:
        reembolso = total_pagado * 0.5
    else:
        reembolso = 0.0

    return round(reembolso, 2)