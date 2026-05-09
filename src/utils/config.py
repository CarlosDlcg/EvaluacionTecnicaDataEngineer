from dotenv import load_dotenv
import os

load_dotenv()

LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
TIMEZONE = os.getenv("TIMEZONE")

BASE_URL = os.getenv("BASE_URL")
HOURLY_FIELDS = os.getenv("HOURLY_FIELDS")

DB_PATH = os.getenv("DB_PATH")