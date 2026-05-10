import os
import pandas as pd

from src.utils.logger import setup_logger

logger = setup_logger(
    "transformation_logger",
    "transformation.log"
)


class WeatherTransformation:

    def transform_data(self, data):

        logger.info("Iniciando transformación de datos")

        # Convertimos a DataFrame
        df = pd.DataFrame(data)

        # Convertimos el campo time a datetime
        df["time"] = pd.to_datetime(df["time"])

        # Renombramos columnas
        df.rename(
            columns={
                "time": "fecha",
                "temperature_2m": "temperatura_c",
                "precipitation": "precipitacion_mm"
            },
            inplace=True
        )

        # Filtramos horas entre 06:00 y 22:00
        df = df[
            (df["fecha"].dt.hour >= 6) &
            (df["fecha"].dt.hour <= 22)
        ]

        logger.info(
            "Filtrado de horarios aplicado correctamente"
        )

        # Detectamos valores nulos o negativos
        invalid_records = df[
            (
                df[[
                    "temperatura_c",
                    "precipitacion_mm"
                ]].isnull().any(axis=1)
            )
            |
            (
                df[[
                    "temperatura_c",
                    "precipitacion_mm"
                ]] < 0
            ).any(axis=1)
        ]

        logger.warning(
            f"Se encontraron "
            f"{len(invalid_records)} registros inválidos"
        )

        # Eliminamos registros inválidos
        clean_df = df.drop(invalid_records.index)

        logger.info(
            f"DataFrame limpio con {len(clean_df)} registros"
        )

        logger.info(
            "Transformación de datos finalizada"
        )

        return clean_df

    def save_csv(self, dataframe):

        os.makedirs("data/final", exist_ok=True)

        file_path = (
            "data/final/datos_clima_cdmx.csv"
        )

        dataframe.to_csv(
            file_path,
            index=False
        )

        logger.info(
            f"CSV exportado correctamente en {file_path}"
        )

        return file_path