# language: es
Característica: Cálculo del total de la renta
  Como capitán
  Quiero saber cuánto pagaré por la renta
  Para decidir si reservo

  Escenario esquema: Total según horario, día y árbitro
    Dado una renta de <horas> hora(s) que inicia a las <hora_inicio>
    Y es <dia_semana>
    Y el árbitro <arbitro>
    Cuando se calcula el total
    Entonces el total es <total>

    Ejemplos:
      | horas | hora_inicio | dia_semana | arbitro | total  |
      | 1     | 10:00       | lunes      | no      | 800    |
      | 1     | 17:59       | lunes      | no      | 800    |
      | 1     | 18:00       | lunes      | no      | 1050   |
      | 1     | 10:00       | sabado     | no      | 920    |
      | 1     | 18:00       | sabado     | no      | 1207.5 |
      | 1     | 10:00       | domingo    | si      | 1170   |