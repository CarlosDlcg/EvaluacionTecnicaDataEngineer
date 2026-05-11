# Documentación Técnica del Proyecto

## Descripción del Pipeline

El proyecto consiste en un pipeline ETL modular desarrollado en Python para obtener información climática desde la API de Open-Meteo. El pipeline extrae datos meteorológicos de la Ciudad de México, almacena la respuesta original de la API, parsea esta respuesta, transforma los datos utilizando Pandas y posteriormente los carga en una base de datos SQLite para realizar consultas analíticas mediante SQL.

La etapa de ingestión obtiene los datos desde la API y realiza validaciones de conexión, status code y formato JSON. Posteriormente, la etapa de transformación limpia y procesa la información, incluyendo conversión de fechas, filtrado de horarios y validación de registros inválidos. Después de la transformación, se genera un archivo CSV con los datos limpios para su posterior carga en SQLite. Finalmente, la etapa de carga almacena los datos del archivo CSV en SQLite para su análisis.

---

# Decisiones Técnicas

## Arquitectura Modular

El pipeline fue dividido en módulos independientes (`ingestion`, `transformation`, `load` y `utils`) para separar responsabilidades y facilitar mantenimiento, escalabilidad y pruebas individuales de cada componente.

## Manejo de Errores

Cada módulo implementa su propio manejo de excepciones y logging para encapsular errores específicos de cada etapa del pipeline. Además, se implementó logging modular mediante archivos independientes para ingestion, transformación, carga y orquestación general del pipeline.

## Uso de Pandas y SQLite

Pandas fue utilizado para realizar las transformaciones tabulares y validaciones de datos debido a su simplicidad y flexibilidad para procesamiento de datasets pequeños y medianos. SQLite fue seleccionado como motor de persistencia por ser una solución ligera, portable y suficiente para el alcance de la evaluación técnica.

## Configuración Externalizada

La configuración del proyecto fue desacoplada del código utilizando variables de entorno (`.env`) para facilitar portabilidad y mantenibilidad.

---

# Mejoras Futuras

Si tuviera más tiempo, implementaría:
- pruebas automatizadas por módulo
- exportación en formato Parquet
- Dockerización del pipeline
- validaciones adicionales de calidad de datos
- orquestación del pipeline mediante herramientas como Apache Airflow
- separación futura de componentes como servicios independientes para mejorar escalabilidad y mantenimiento