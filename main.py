from src.sakila_ETL import run_etl

if __name__ == "__main__":
    # Ejecuta el pipeline ETL completo: extrae -> transforma -> exporta CSV y genera Excel
    run_etl()