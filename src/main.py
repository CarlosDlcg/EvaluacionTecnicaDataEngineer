from src.ingestion.weather_ingestion import WeatherIngestion
from src.transformation.weather_transformation import WeatherTransformation
from src.utils.logger import logger


def main():

    try:

        ingestion = WeatherIngestion()

        raw_data, processed_data = ingestion.fetch_weather_data()

        raw_path = ingestion.save_raw_data(raw_data)

        processed_path = ingestion.save_processed_data(processed_data)

        transformation = WeatherTransformation()

        transformed_df = transformation.transform_data(processed_data)

        csv_path = transformation.save_csv(transformed_df)

        logger.info(
            "Pipeline ejecutado exitosamente"
        )

        print(f"Raw data: {raw_path}")
        print(f"Processed data: {processed_path}")
        print(f"CSV final: {csv_path}")

    except Exception as e:

        logger.error(
            f"La ejecución del pipeline falló: {e}"
        )

        print(f"Error: {e}")


if __name__ == "__main__":
    main()