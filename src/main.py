from src.ingestion.weather_ingestion import WeatherIngestion
from src.utils.logger import logger


def main():

    try:
        ingestion = WeatherIngestion()

        raw_data, processed_data = ingestion.fetch_weather_data()

        raw_path = ingestion.save_raw_data(raw_data)

        processed_path = (
            ingestion.save_processed_data(processed_data)
        )

        logger.info("Ingestión del pipeline completada exitosamente")

        print(f"Datos brutos almacenados en: {raw_path}")
        print(f"Datos procesados almacenados en: {processed_path}")

    except Exception as e:
        logger.error(f"La ejecución del pipeline falló: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()