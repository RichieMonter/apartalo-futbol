# 6. Pruebas de aceptación y TDD
> Ejercicio 6 · Tema 8 · 🎩 desarrollador

## 6.2 Mis ciclos de TDD

| Ciclo | Commit ROJO | Commit VERDE | Commit REFACTOR | Qué aprendí |
|---|---|---|---|---|
| 1 (R2) | `ROJO: cancelación con 5.99 h espera 0` | `VERDE: reembolso 0% con menos de 6 h` | — | Que el límite `>= 6` vs `> 6` importa. |
| 2 (R2) | `ROJO: cancelación con 6 h espera 50%` | `VERDE: reembolso 50% en [6, 24)` | `REFACTOR: extraer UMBRAL_24H y UMBRAL_6H` | Los umbrales merecen nombre propio. |
| 3 (R1) | `ROJO: renta a las 18:00 espera $1050` | `VERDE: tarifa nocturna desde las 18:00` | `REFACTOR: convertir hora a minutos` | Comparar floats directamente es frágil. |

## 6.6 Cobertura de caminos

- **Función:** `calcular_reembolso(monto, horas)`.
- **Caminos:** 4 → (1) `return monto` (100 %), (2) `return monto * 0.5` (50 %), (3) `return 0` (0 %), (4) `raise ValueError` (monto < 0 o horas < 0).
- **Caminos que recorren mis pruebas:** 4 de 4.
- **Cobertura:** 100 %.
- **Pruebas que agregué para completar:** `test_reembolso_monto_negativo_lanza_value_error` y `test_reembolso_horas_negativas_lanza_value_error`.

## 6.7 Regresión

- **Defecto (provocado):** cambié `>= 6` por `> 6` en `calcular_reembolso`.
- **Prueba que lo detecta:** `test_reembolso_50_por_ciento_exactamente_6h` (fila `| 800 | 6 | 400 |` de la tabla FIT).
- **Qué pasaba y cómo lo corregí:** con `> 6`, la fila de 6 h devolvía 0 en vez de 400. Regresé el operador a `>=` y la prueba volvió a verde. Dejé la prueba de regresión en `tests/unitarias/test_reembolso_regresion.py`.
