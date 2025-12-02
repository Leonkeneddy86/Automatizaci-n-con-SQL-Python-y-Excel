# src/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar .env en la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]
dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path)

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "sakila")

# CONEXION para SQLAlchemy usando mysql-connector-python
SQLALCHEMY_DATABASE_URI = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Rutas de salida / exportar .csv y .xlsx
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DASHBOARD_DIR = BASE_DIR / "dashboard"
DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)

CSV_PATH = OUTPUT_DIR / "datos_sakila.csv"
EXCEL_PATH = DASHBOARD_DIR / "sakila_dashboard.xlsx"