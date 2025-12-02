# main.py
from src.sakila_ETL import run_etl

if __name__ == "__main__":
    # Ejecuta sakila_ETL completo: extrae -> transforma -> exporta CSV y xlsx para EXCEL
    run_etl()