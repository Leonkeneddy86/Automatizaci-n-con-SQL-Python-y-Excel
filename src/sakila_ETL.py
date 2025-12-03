# Proceso de ETL para la base de datos Sakila
import pandas as pd
from sqlalchemy import create_engine
import os
from config import *

def conectar_bd():

    url = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(url)
    return engine

def extraer_datos():

    print("Conectando a la base de datos...")
    
    engine = conectar_bd()

    # Query para análisis de clientes
    query = """
    SELECT 
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) as cliente,
        c.email,
        c.active,
        a.address,
        a.district,
        a.postal_code,
        ci.city,
        co.country,
        DATE(r.rental_date) as fecha_renta,
        DATE(r.return_date) as fecha_devolucion,
        p.amount as monto,
        DATE(p.payment_date) as fecha_pago
    FROM customer c
    JOIN address a ON c.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
    JOIN rental r ON c.customer_id = r.customer_id
    JOIN payment p ON p.rental_id = r.rental_id
    """   
    df = pd.read_sql(query, engine)
    print(f"✓ {len(df)} registros extraídos")
    return df

def transformar_datos(df):

    print("Transformando datos...")

    df['monto'] = df['monto'].astype(float)
    df['fecha_renta'] = pd.to_datetime(df['fecha_renta'])
    df['fecha_devolucion'] = pd.to_datetime(df['fecha_devolucion'])
    df['fecha_pago'] = pd.to_datetime(df['fecha_pago'])
    df['año_renta'] = pd.to_datetime(df['fecha_renta']).dt.year
    df['mes_renta'] = pd.to_datetime(df['fecha_renta']).dt.month
    df['dia_semana'] = pd.to_datetime(df['fecha_renta']).dt.day_name()
    df['estado_cliente'] = df['active'].map({1: 'Activo', 0: 'Inactivo'})
    df['mes_año'] = pd.to_datetime(df['fecha_renta']).dt.to_period('M').astype(str)

    print("✓ Transformación completada")

    return df

def cargar_datos(df):

    print("💾 Guardando CSV...")


    # Guardar CSV
    df.to_csv(f'{OUTPUT_FOLDER}/datos_sakila.csv', index=False, encoding='utf-8-sig')

    print(f"✓ CSV guardado en '{OUTPUT_FOLDER}/datos_sakila.csv'")

    return True

def ejecutar_etl():

    """Ejecutar proceso ETL completo"""
    try:
        # Extraer
        df = extraer_datos()
        
        # Transformar
        df_transformado = transformar_datos(df)
        
        # Guardar CSV principal
        cargar_datos(df_transformado)
        
        # Retornar dataset para el dashboard
        return {
            'datos_principales': df_transformado
        }
    except Exception as e:
        print(f"❌ Error: {e}")
        return None
    
if __name__ == "__main__":
        ejecutar_etl()