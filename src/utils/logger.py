import logging
import os

from src.utils.config import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)


def setup_logger(name, log_file, console_output=False):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    # Evitamos handlers duplicados
    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(
            f"{LOG_DIR}/{log_file}"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        # Logs en consola solo si se solicita
        if console_output:

            stream_handler = logging.StreamHandler()

            stream_handler.setFormatter(formatter)

            logger.addHandler(stream_handler)

    return logger