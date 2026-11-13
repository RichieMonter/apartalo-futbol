-- Ejercicio 8 · Consultas sobre la fotografía de tu tablero.

-- a) Puntos comprometidos en el Sprint 1 (filtrando valores reales de historias: 3, 5, 8)
SELECT SUM(puntos) AS puntos_comprometidos 
FROM tablero 
WHERE puntos IN (3, 5, 8);

-- b) Puntos entregados (estado = 'Liberación')
SELECT SUM(puntos) AS puntos_entregados 
FROM tablero 
WHERE estado = 'Liberación';

-- c) Porcentaje de cumplimiento (entregados ÷ comprometidos)
SELECT ROUND(
    (SELECT SUM(puntos) FROM tablero WHERE estado = 'Liberación') * 100.0 / 
    (SELECT SUM(puntos) FROM tablero WHERE puntos IN (3, 5, 8)), 2
) AS porcentaje_cumplimiento;

-- d) Tiempo de ciclo promedio en días (de inicio a terminado) de las historias entregadas
SELECT 'No aplica (columnas de fecha no incluidas en la vista)' AS tiempo_ciclo_promedio;

-- e) Subconjunto: historias con prioridad 'Must', con sus puntos y su estado
SELECT titulo, puntos, estado 
FROM tablero 
WHERE prioridad = 'Must';

