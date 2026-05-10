# Documentación Técnica del Proyecto

## Descripción General

Se desarrolló un pipeline ETL modular en Python para extraer información climática desde la API de Open-Meteo, transformar los datos utilizando Pandas, almacenarlos en SQLite y ejecutar consultas analíticas mediante SQL.

El objetivo principal fue construir una solución simple, mantenible y estructurada, aplicando conceptos fundamentales de Ingeniería de Datos.

---

# Flujo del Pipeline

```text
Open-Meteo API
       │
       ▼
Data Ingestion
       │
       ▼
Raw JSON Storage
Parsed JSON Storage
       │
       ▼
Data Transformation
       │
       ▼
CSV Export
       │
       ▼
SQLite Load
       │
       ▼
SQL Analytics
```

---

# Decisiones Técnicas

## Arquitectura Modular

El pipeline fue dividido en módulos independientes para separar responsabilidades y facilitar mantenimiento, escalabilidad y pruebas individuales:
- ingestion/
- transformation/
- load/
- utils/

Cada módulo encapsula su propia lógica, manejo de errores y logging.

## Separación por Capas de Datos

Se decidió almacenar los datos en distintas etapas del pipeline:
- raw/: respuesta original de la API.
- processed/: datos parseados.
- final/: datos limpios exportados a CSV.
- database/: persistencia SQLite.

Esto permite trazabilidad, reprocesamiento y mejor organización del flujo de datos.

## Configuración Externalizada

La configuración del proyecto fue desacoplada del código utilizando variables de entorno (.env) para mejorar portabilidad y mantenibilidad.

Entre los parámetros configurables se encuentran:
- endpoint de la API
- coordenadas
- campos solicitados
- rutas de logs
- ubicación de la base de datos

## Logging Modular

Se implementó logging independiente para cada etapa del pipeline:
- ingestion.log
- transformation.log
- loader.log
- pipeline.log

Esto facilita debugging, monitoreo y observabilidad del sistema.

## Uso de SQLite

SQLite fue utilizado como motor de persistencia por ser una solución ligera, portable y suficiente para el alcance de la evaluación técnica.

---

# Dificultades Encontradas

## Manejo de Imports y Modularidad

Inicialmente surgieron problemas relacionados con imports entre módulos y ejecución del proyecto. Se resolvió utilizando imports absolutos y ejecutando el pipeline mediante:

```bash
python -m src.main
```

## Separación Correcta entre Datos Raw y Processed

En una primera versión, los datos transformados eran almacenados como datos raw. Posteriormente se corrigió separando claramente:
- respuesta original de la API
- datos procesados

## Manejo de JSON Inválido

Se identificó la necesidad de validar explícitamente respuestas JSON inválidas para evitar fallos silenciosos durante el procesamiento de datos.

## Organización del Logging

Inicialmente todos los módulos escribían en un único archivo de logs. Posteriormente se implementó logging modular por componente para mejorar trazabilidad y depuración.
