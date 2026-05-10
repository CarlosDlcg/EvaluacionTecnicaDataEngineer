import os
import sqlite3
import pandas as pd

from src.utils.config import DB_PATH
from src.utils.logger import setup_logger

logger = setup_logger(
    "loader_logger",
    "loader.log"
)


class WeatherLoader:

    def load_to_sqlite(self, csv_path):

        logger.info(
            "Iniciando carga de datos hacia SQLite"
        )

        os.makedirs("data/database", exist_ok=True)

        db_path = DB_PATH

        try:

            # Leemos el CSV
            df = pd.read_csv(csv_path)

            logger.info(
                f"CSV leído correctamente "
                f"con {len(df)} registros"
            )

            # Conexión SQLite
            with sqlite3.connect(db_path) as connection:

                logger.info(
                    "Conexión SQLite establecida"
                )

                df.to_sql(
                    "clima_cdmx",
                    connection,
                    if_exists="replace",
                    index=False
                )

                logger.info(
                    "Datos cargados correctamente "
                    "en la tabla clima_cdmx"
                )


            logger.info(
                "Conexión SQLite finalizada correctamente"
            )

            return db_path

        except Exception as e:

            logger.error(
                f"Error durante la carga SQLite: {e}"
            )

            raise RuntimeError(
                f"Falló la carga a SQLite: {e}"
            )