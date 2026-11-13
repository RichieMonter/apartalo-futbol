# 4. Refinamiento y escenarios
> Ejercicio 4 · Tema 7 · 🎩 PO y 🎩 desarrollador
> Los escenarios BDD van en la carpeta `features/`.

## 4.1 Pesar (MoSCoW)

**Criterio que usé:** 
Clasifiqué como **Must** todas las reglas de negocio core (R1, R2, R3 y el RNF de robustez) porque sin ellas la app no resuelve el problema principal de Chuy (cobrar mal, reembolsar mal o guardar datos corruptos). Dejé como **Should** y **Could** las funciones de conveniencia (como dividir el pago o los colores del equipo) y mandé a **Won't** la renta nocturna porque el cliente aún no ha tomado la decisión de negocio.

## 4.2 Ilustrar

**Historia:** #2 (Cálculo de renta base según horario y fin de semana).
**Boceto:** Representación de la pantalla donde el capitán selecciona la cancha, la fecha, la hora de inicio y si requiere árbitro, mostrando el desglose del total en la parte inferior.
![boceto](img/boceto_renta.png)

## 4.3 Medir (Size)

Utilicé la serie de Fibonacci (1, 2, 3, 5, 8, 13, 21) para asignar puntos a todas las historias en el campo "Puntos" de GitHub, evaluando la complejidad lógica y la cantidad de pruebas TDD necesarias.

## 4.4 Dividir (Split)

- **Velocidades de referencia de mi variante:** 24, 20 y 25 puntos.
- **Operación:** Promedio de velocidad = (24 + 20 + 25) / 3 = 23.
- **Carga máxima por historia:** 23 / 2 = 11.5 puntos. (Ninguna historia debe superar los 11 puntos).
- **Historias que rebasan la carga máxima:** Ninguna historia individual (la máxima es de 8 puntos), pero la **Épica B** sí rebasaba la carga por ser muy grande, así que se dividió.

| Historia original | Puntos | Subhistorias (issues) | Puntos de cada una | ¿Cómo la partí? |
|---|---|---|---|---|
| Épica B (Panel admin) #15 | 13+ | #10 Pantalla informativa, #11 Módulo nocturno | 3 y 3 | Por flujo de valor: separé la vista pública de la entrada (para los jugadores) del análisis interno de costos de luz (para el administrador). |

## 4.6 R2 como tabla FIT

> R2 (Cancelación): 24h o más = 100%; entre 6h y 23.9h = 50%; menos de 6h = 0%.

| Anticipación de cancelación (horas) | Monto pagado ($) | Resultado esperado ($) | Resultado real ($) |
|---|---|---|---|
| 24 | 800 | 800.00 | ✅ 800.00 |
| 48 | 1050 | 1050.00 | ✅ 1050.00 |
| 12 | 800 | 400.00 | ✅ 400.00 |
| 6 | 1050 | 525.00 | ✅ 525.00 |
| 5.99 | 800 | 0.00 | ✅ 0.00 |
| -1 (inválido) | 800 | ValueError | ✅ ValueError |