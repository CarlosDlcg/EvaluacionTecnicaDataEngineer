import requests
import json
import os

from datetime import datetime

from src.utils.config import LATITUDE, LONGITUDE, TIMEZONE, BASE_URL, HOURLY_FIELDS
from src.utils.logger import setup_logger

logger = setup_logger(
    "ingestion_logger",
    "ingestion.log"
)


class WeatherIngestion:

    def fetch_weather_data(self):

        params = {
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "hourly": HOURLY_FIELDS,
            "timezone": TIMEZONE
        }

        try:

            logger.info("Inicializando la petición a la API")

            response = requests.get(
                BASE_URL,
                params=params,
                timeout=30
            )

            # Verificamos el status code de la respuesta
            if response.status_code != 200:

                logger.error(
                    f"La API respondió con el status code "
                    f"{response.status_code}"
                )

                raise RuntimeError(
                    f"La respuesta de la API falló con el "
                    f"status {response.status_code}"
                )

            logger.info("La petición a la API fue exitosa")

            try:

                raw_data = response.json()

            except json.JSONDecodeError:

                logger.error(
                    "La API devolvió un JSON inválido"
                )

                raise ValueError(
                    "La respuesta de la API no contiene "
                    "un JSON válido"
                )

            # Parseamos los campos necesarios
            parsed_data = self.parse_weather_data(raw_data)

            return raw_data, parsed_data

        except requests.exceptions.Timeout:

            logger.error(
                "La petición a la API excedió el tiempo de espera"
            )

            raise TimeoutError(
                "La petición a la API excedió el tiempo de espera"
            )

        except requests.exceptions.ConnectionError:

            logger.error(
                "Error de conexión al intentar conectar con la API"
            )

            raise ConnectionError(
                "Fallo al conectar con la API"
            )

        except requests.exceptions.RequestException as e:

            logger.error(f"Error en la petición: {e}")

            raise RuntimeError(
                f"La petición a la API falló: {e}"
            )

    def parse_weather_data(self, data):

        try:

            hourly_data = data["hourly"]

            parsed_data = [
                {
                    "time": time,
                    "temperature_2m": temp,
                    "precipitation": precip
                }
                for time, temp, precip in zip(
                    hourly_data["time"],
                    hourly_data["temperature_2m"],
                    hourly_data["precipitation"]
                )
            ]

            logger.info(
                f"Se han parseado "
                f"{len(parsed_data)} registros climáticos"
            )

            return parsed_data

        except KeyError as e:

            logger.error(
                f"Campo esperado no encontrado: {e}"
            )

            raise ValueError(
                f"Error al analizar el JSON. "
                f"Campo faltante: {e}"
            )
    
    def save_raw_data(self, data):

        os.makedirs("data/raw", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_path = (
            f"data/raw/weather_raw_{timestamp}.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        logger.info(f"Datos guardados en {file_path}")

        return file_path
    
    def save_processed_data(self, data):

        os.makedirs("data/processed", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_path = (
            f"data/processed/weather_processed_{timestamp}.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        logger.info(
            f"Datos procesados guardados en {file_path}"
        )

        return file_path