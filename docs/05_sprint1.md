# 5. Sprint 1 (27 oct – 9 nov 2026)
> Ejercicio 5 · Temas 4 y 11

## A. Planeación del sprint

**Objetivo del sprint:** Implementar y probar R1 (cálculo de renta) y R2 (reembolso por cancelación) con TDD, dejando el tablero y el backlog listos para el Sprint 2.

**Capacidad en horas (Figura 2 del Tema 11):**

| Concepto | Horas |
|---|---|
| Horas disponibles en las dos semanas (8 h/día × 5 días × 2 semanas) | 80 |
| − Otras actividades (clases, trabajo, tareas) | 40 |
| = Disponibilidad | 40 |
| ÷ 2 = **Capacidad** | **20 h** |

**Compromiso (historias del Sprint 1):**

| Historia | Puntos | Horas estimadas |
|---|---|---|
| #1 Calcular total renta (R1) | 8 | 6 |
| #4 Cancelar y reembolsar (R2) | 8 | 6 |
| #7 Validar R3 (horas completas / máx 2) | 3 | 3 |
| #10 ValueError en entradas inválidas (RNF) | 3 | 3 |
| **Total** | **22** | **18 h** |

**Definición de Terminado (DoD):**
1. Código en `src/apartalo/reglas.py` con docstrings.
2. Pruebas unitarias en `tests/unitarias/` con `pytest` pasando.
3. Pruebas de aceptación en `tests/aceptacion/` con `@pytest.mark.parametrize`.
4. `pytest` en verde al 100 % en `main`.
5. `docs/06_tdd.md` actualizado con los commits de los ciclos.

**DoD vs. criterios de aceptación:** el DoD aplica a **todas** las historias (código probado, documentado, en main). Los criterios de aceptación son específicos de **una** historia. Ejemplo: la historia #1 tiene criterios de aceptación sobre el recargo de fin de semana y el árbitro opcional; el DoD exige además que tenga docstring y prueba unitaria.

## B. Junta diaria — bitácora

### 27 oct 2026
- **¿Qué hice?** Creé los issues del backlog y configuré el tablero con WIP.
- **¿Qué haré?** Empezar el TDD de R2 (cancelación).
- **¿Qué me lo impide?** Nada.

### 28 oct 2026
- **¿Qué hice?** Ciclo ROJO de R2: prueba de cancelación con menos de 6 h.
- **¿Qué haré?** Ciclo VERDE de R2.
- **¿Qué me lo impide?** Duda con el redondeo a 2 decimales.

### 30 oct 2026
- **¿Qué hice?** R2 completa (100 %, 50 %, 0 %). Ciclo REFACTOR extrayendo la constante de umbrales.
- **¿Qué haré?** Empezar R1 (cálculo de renta).
- **¿Qué me lo impide?** Nada.

### 3 nov 2026
- **¿Qué hice?** Avancé R1 hasta el recargo de fin de semana.
- **¿Qué haré?** Cerrar R1 con la prueba del límite exacto 17:59 vs 18:00.
- **¿Qué me lo impide?** No tenía claro cómo manejar la hora como `float` (18.5). Lo resolví convirtiendo la hora a minutos desde las 00:00.

### 5 nov 2026
- **¿Qué hice?** R1 completa con tabla de ejemplos y tabla FIT pasando.
- **¿Qué haré?** Escribir `docs/06_tdd.md` y preparar la revisión.
- **¿Qué me lo impide?** Nada.

### 7 nov 2026
- **¿Qué hice?** Documentación de TDD, cobertura de caminos y prueba de regresión.
- **¿Qué haré?** Preparar capturas y revisión del sprint.
- **¿Qué me lo impide?** Falta correr `metricas/cargar_tablero.py`.

**Impedimentos y qué hizo el SM:**

| Fecha | Impedimento | Qué hizo el SM |
|---|---|---|
| 30 oct | Duda con el redondeo a 2 decimales | El SM acordó usar `round(x, 2)` en todas las salidas de dinero y lo agregó al DoD. |
| 3 nov | Manejo de la hora como `float` | El SM propuso convertir la hora a minutos desde las 00:00 para evitar comparaciones de flotantes. |

## C. Revisión del sprint

| Historia | ¿Cumple sus criterios? | ¿Aceptada? | Evidencia |
|---|---|---|---|
| #1 Calcular total renta (R1) | Sí | ✅ | Commit `VERDE: cobra $1050 con hora >= 18:00` + `pytest -m aceptacion` en verde |
| #4 Cancelar y reembolsar (R2) | Sí | ✅ | Commit `VERDE: reembolso 50% en [6, 24)` + tabla FIT |
| #7 Validar R3 | Sí | ✅ | Prueba unitaria `test_horas_invalidas` en `tests/unitarias/` |
| #10 ValueError | Sí | ✅ | Prueba `test_entradas_invalidas_lanzan_value_error` en `tests/rnf/` |

**Cambio que pediría mi cliente → historia nueva:** Chuy vio la tabla FIT y pidió que el reembolso también se calcule cuando la reserva se cancela por lluvia (fuerza mayor). Lo convierto en el issue **#14 "Como administrador, quiero reembolsar el 100 % si se cancela por lluvia"** y lo dejo para el Sprint 2.

## D. Retrospectiva

**¿Qué salió bien?** El TDD me obligó a pensar en los límites exactos (24 h, 6 h, 17:59, 18:00) antes de codificar; la tabla FIT detectó un error de redondeo que no había visto.

**¿Qué hay que mejorar?** Subestimé el tiempo de la documentación; la bitácora diaria la llené con retraso.

**Acciones para el Sprint 2:**
1. Bloquear 30 min al final de cada día para la bitácora.
2. Escribir la prueba de aceptación antes que la unitaria, siempre.
