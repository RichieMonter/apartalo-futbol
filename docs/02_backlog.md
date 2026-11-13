# 2. El product backlog
> Ejercicio 2 · Tema 6 · 🎩 PO
> Las historias van como **issues** (formulario "Historia de usuario"). Aquí va lo demás.

## 2.1 Roles

| Rol | Quién es | Qué desea |
|---|---|---|
| **Capitán** | Líder del equipo que hace la reserva y recolecta el dinero de sus jugadores. | Reservar rápido, saber el total y dividir el pago entre su equipo. |
| **Jugador** | Integrante del equipo que paga su parte. | Saber cuánto le toca y que la reserva exista. |
| **Administrador (Chuy)** | Dueño de las 2 canchas. | Evitar reservas cruzadas y cancelaciones sin aviso, y ver la agenda del día. |
| **Sistema (no humano)** | El backend de Apártalo. | Calcular totales, reembolsos y validar entradas inválidas. |

## 2.2 + 2.3 Historias (issues) y Épicas (issues)

Creados en GitHub con la etiqueta `historia` (y INVEST revisado):

| Issue | Historia (Como… quiero… para…) | Cubre | Puntos | Prioridad |
|---|---|---|---|---|
| #2 | Como **capitán**, quiero **calcular el total de la renta** según hora y día, para saber cuánto pagaré antes de reservar. | R1 | 8 | Must |
| #3 | Como **capitán**, quiero **contratar árbitro opcional** y que se sume al total, para no hacer cuentas a mano. | R1 | 8 | Must |
| #4 | Como **administrador**, quiero **cobrar recargo de fin de semana (15 %)** automáticamente, para no ajustar precios manualmente. | R1 | 8 | Must |
| #5 | Como **capitán**, quiero **cancelar una reserva y saber cuánto me reembolsan** según la anticipación, para decidir si cancelo. | R2 | 5 | Must |
| #6 | Como **administrador**, quiero **validar que la cancelación aplique el porcentaje correcto**, para no regalar dinero. | R2 | 5 | Must |
| #7 | Como **administrador**, quiero **reservar solo por horas completas y máximo 2 horas seguidas**, para respetar la regla del negocio. | R3 | 3 | Should |
| #8 | Como **administrador**, quiero **visualizar los colores del equipo favorito en la interfaz**, para personalizar la app. | Solución | 3 | Could |
| #9 | Como **capitán**, quiero **dividir el pago entre los jugadores** de mi equipo, para no adelantar el dinero. | Solución | 5 | Could |
| #10 | Como **administrador**, quiero **ver la pantalla informativa de partidos** en la entrada, para que los equipos confirmen su horario. | Solución | 3 | Could |
| #11 | Como **administrador**, quiero **consultar la disponibilidad nocturna y costos de luz**, para decidir si rento de noche. | Solución | 3 | Could |
| #12 | Como **administrador**, quiero **registrar capitanes de equipos frecuentes**, para darles un trato preferencial. | Solución | 5 | Could |
| #13 | Como **capitán**, quiero **ver el historial de partidos jugados** de mi equipo, para llevar un control. | Solución | 3 | Could |

**Épicas** (etiqueta `epica`, van al fondo del backlog):
*   **#14 — Épica A (Renta noche):** Analizar costos de luz y decidir si conviene ofrecer horario nocturno con tarifa diferenciada. *(Prioridad: Won't para este sprint)*.
*   **#XX — Épica B (Panel completo del administrador):** Calendario visual, filtros por cancha y fecha, exportación, y notificaciones automáticas. *(Prioridad: Could)*.

**Requisitos No Funcionales (RNF)** (etiqueta `rnf`, formulario "Requisito no funcional"):
*   **#XX — RNF Robustez (Interna):** El sistema debe lanzar `ValueError` en el 100% de entradas inválidas. *(Sprint 1)*.
*   **#XX — RNF Desempeño (Externa):** Calcular 35 reembolsos en menos de 1 segundo en hora pico.
*   **#XX — RNF Usabilidad (Externa):** Completar una reserva en ≤ 3 clics desde la pantalla principal.

## 2.4 Plantilla invertida: historias que me faltaban

`Para poder <beneficio>, como <rol>, quiero <deseo>`

| Beneficio que revisé | Historia que encontré | Issue |
|---|---|---|
| Evitar que el capitán adelante dinero | Para **poder cobrar rápido a mi equipo**, como **capitán**, quiero **dividir el pago entre los jugadores**. | #9 |
| Confirmar horarios sin llamar a Chuy | Para **poder confirmar mi horario sin preguntar**, como **jugador**, quiero **ver la pantalla informativa de partidos**. | #10 |

**¿Cómo me ayudó ordenar por beneficio?** 
Me di cuenta de que la pantalla de agenda (solución visible) esconde dos beneficios distintos: uno para el administrador (control de la entrada) y otro para el jugador (confirmación de su horario). Al enfocarme en el beneficio del jugador, me di cuenta de que necesitaba ver su historial de partidos para sentirse parte del equipo, así que agregué la historia #13.

## 2.5 Glosario (lenguaje ubicuo)

| Término | Qué significa para mi cliente |
|---|---|
| **Cancha** | Campo de fútbol 7 de pasto sintético (tiene 2 canchas en el negocio). |
| **Renta** | Pago por hora de uso de la cancha (varía si es antes o después de las 18:00). |
| **Capitán** | Líder del equipo que aparta la cancha y coordina el pago con sus jugadores. |
| **Reembolso** | Dinero que se le devuelve al capitán al cancelar, dependiendo de las horas de anticipación. |
| **Árbitro** | Persona que dirige el partido; es un servicio opcional con costo extra de $250. |
| **Hora pico** | Viernes de 19:00 a 21:00, donde hay hasta 35 reservas por hora. |

## 2.6 El iceberg

- **En la punta:** Reservar, calcular el total de la renta y cancelar. Es lo que Chuy (el cliente) ve, pide y usa en su día a día.
- **En el fondo:** Las reglas de negocio complejas (R1, R2, R3), las validaciones de errores (`ValueError`), la lógica exacta de reembolsos por horas, la división del pago, el análisis de costos de luz y la base de datos.
- **Por qué:** La interfaz es solo la cáscara visual. Si la lógica de negocio (el fondo del iceberg) no está bien programada y probada con TDD, la app cobrará mal, reembolsará mal y Chuy terminará perdiendo dinero y clientes.