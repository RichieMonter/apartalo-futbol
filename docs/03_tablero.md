# 3. El tablero kanban
> Ejercicio 3 · Tema 3 · 🎩 SM

## 3.2 Límites WIP

| Columna | Límite | Por qué ese número |
|---|---|---|
| Aceptación | 2 | Soy una sola persona; no puedo validar más de 2 historias a la vez sin dejar de codificar. |
| Desarrollo | 2 | Un WIP de 2 historias permite avanzar una mientras la otra espera una decisión, sin dispersarme. |
| Pruebas | 2 | El TDD se hace historia por historia; más de 2 en pruebas significa que estoy acumulando deuda. |

## 3.3 Políticas explícitas

| Para pasar a… | La tarjeta debe cumplir… |
|---|---|
| Aceptación | Historia con formato "Como… quiero… para…", al menos 2 criterios de aceptación, INVEST revisado, etiqueta `historia`. |
| Desarrollo | Historia priorizada como Must o Should, estimada en puntos, asignada al campo Sprint. |
| Desarrollo listo | Código en `src/apartalo/reglas.py`, al menos una prueba unitaria pasa localmente. |
| Pruebas | Código mergeado a `main`, pruebas unitarias en verde, `docs/06_tdd.md` con el ciclo ROJO/VERDE enlazado. |
| Pruebas listo | Todas las pruebas unitarias y de aceptación pasan, cobertura de caminos revisada. |
| Liberación | `pytest` en verde al 100 %, commit final pusheado, criterios de aceptación verificados. |

## 3.4 Las seis prácticas de kanban en mi tablero

| Práctica | Cómo la aplico (o por qué todavía no aplica) |
|---|---|
| 1. Visualizar el trabajo | Tablero con 7 columnas; cada historia es una tarjeta del Project. |
| 2. Limitar el WIP | Límites en Aceptación (2), Desarrollo (2) y Pruebas (2). |
| 3. Administrar el flujo | Muevo la tarjeta solo cuando cumple la política; mido tiempo de ciclo con las fechas de inicio y fin. |
| 4. Hacer explícitas las políticas | Documentadas en esta sección y en `docs/03_tablero.md`. |
| 5. Implementar ciclos de retroalimentación | Daily, revisión de sprint, retrospectiva y `pytest` como feedback automático. |
| 6. Mejora colaborativa y evolución experimental | En la retrospectiva ajusto límites WIP y políticas para el Sprint 2. |
