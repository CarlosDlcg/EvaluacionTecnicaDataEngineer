-- A. Temperatura promedio por día
SELECT
    DATE(fecha) AS fecha,
    ROUND(AVG(temperatura_c), 2) AS temperatura_promedio
FROM clima_cdmx
GROUP BY DATE(fecha)
ORDER BY temperatura_promedio DESC;


-- B. Horas con precipitación
SELECT
    fecha,
    precipitacion_mm
FROM clima_cdmx
WHERE precipitacion_mm > 0
ORDER BY fecha ASC;


-- C. Día con mayor variación térmica
SELECT
    DATE(fecha) AS fecha,
    ROUND(MAX(temperatura_c) - MIN(temperatura_c), 2)
        AS variacion_termica
FROM clima_cdmx
GROUP BY DATE(fecha)
ORDER BY variacion_termica DESC
LIMIT 1;


-- D. Resumen diario
SELECT
    DATE(fecha) AS fecha,

    ROUND(MIN(temperatura_c), 2)
        AS temperatura_minima,

    ROUND(MAX(temperatura_c), 2)
        AS temperatura_maxima,

    ROUND(AVG(temperatura_c), 2)
        AS temperatura_promedio,

    ROUND(SUM(precipitacion_mm), 2)
        AS precipitacion_total
FROM clima_cdmx
GROUP BY DATE(fecha)
ORDER BY fecha ASC;