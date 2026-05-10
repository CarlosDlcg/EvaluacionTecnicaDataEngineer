from src.ingestion.weather_ingestion import WeatherIngestion
from src.transformation.weather_transformation import WeatherTransformation
from src.load.weather_loader import WeatherLoader
from src.utils.logger import setup_logger

logger = setup_logger(
    "pipeline_logger",
    "pipeline.log",
    console_output=True
)


def main():

    try:

        logger.info(
            "Iniciando ejecución del pipeline"
        )

        # Etapa de Ingestión
        logger.info(
            "Iniciando etapa de ingestion"
        )
        ingestion = WeatherIngestion()
        raw_data, processed_data = ingestion.fetch_weather_data()
        raw_path = ingestion.save_raw_data(raw_data)
        processed_path = ingestion.save_processed_data(processed_data)
        logger.info(
            "Etapa de ingestion completada"
        )

        # Etapa de Transformación
        logger.info(
            "Iniciando etapa de transformación"
        )
        transformation = WeatherTransformation()
        transformed_df = transformation.transform_data(processed_data)
        csv_path = transformation.save_csv(transformed_df)
        logger.info(
            "Etapa de transformación completada"
        )

        # Etapa de Carga
        logger.info(
            "Iniciando etapa de carga SQLite"
        )
        loader = WeatherLoader()
        db_path = loader.load_to_sqlite(csv_path)
        logger.info(
            "Etapa de carga completada"
        )


        logger.info(
            "Pipeline ejecutado exitosamente"
        )
        print(f"Datos en bruto: {raw_path}")
        print(f"Datos procesados: {processed_path}")
        print(f"CSV final: {csv_path}")
        print(f"Base de datos SQLite: {db_path}")

    except Exception as e:

        logger.error(
            f"La ejecución del pipeline falló: {e}"
        )

        print(f"Error: {e}")


if __name__ == "__main__":
    main()