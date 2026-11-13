# language: es
Característica: Reembolso por cancelación de reserva

  Esquema del escenario: Calcular el reembolso según las horas de anticipación
    Dado que el usuario pagó un total de <total_pagado> y cancela con <horas> horas de anticipación
    Cuando se procesa el reembolso
    Entonces el monto devuelto es de <reembolso_esperado> pesos

    Ejemplos:
      | total_pagado | horas | reembolso_esperado |
      | 1000.0       | 30.0  | 1000.0             |
      | 1000.0       | 24.0  | 1000.0             |
      | 1000.0       | 12.0  | 500.0              |
      | 1000.0       | 6.0   | 500.0              |
      | 1000.0       | 4.0   | 0.0                |
      | 1000.0       | 0.0   | 0.0                |