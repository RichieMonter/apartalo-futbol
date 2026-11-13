# language: es
Característica: Cálculo del total de la renta de la cancha

  Esquema del escenario: Calcular el costo de la renta según el horario, fin de semana y árbitro
    Dado que la renta de la cancha inicia a las <hora> horas con fin de semana <fin_semana> y opción de árbitro <arbitro>
    Cuando se calcula el total de la renta
    Entonces el monto a pagar debe ser de <esperado> pesos

    Ejemplos:
      | hora | fin_semana | arbitro | esperado |
      | 15   | falso      | falso   | 800.0    |
      | 19   | falso      | falso   | 1050.0   |
      | 10   | verdadero  | verdadero| 1170.0  |