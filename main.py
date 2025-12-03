# main.py
# ⭐ PUNTO DE ENTRADA PRINCIPAL DEL PROYECTO
# Ejecuta la automatización completa: MySQL → Python → CSV → Excel

import os
import sys
from datetime import datetime
from pathlib import Path
 

# Agregar la carpeta src al path de Python
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from src.sakila_ETL import ejecutar_etl
from src.config import EXCEL_FILE, AUTO_OPEN_EXCEL, OUTPUT_FOLDER

def main():
    """
    Ejecutar proceso completo de automatización Sakila
    
    Flujo:
    1. Extrae datos de MySQL (base de datos Sakila)
    2. Transforma los datos con Pandas
    3. Guarda archivos CSV en carpeta output/
    4. Abre Excel automáticamente (si está configurado)
    """
    print("\n" + "="*50)
    print("🚀 AUTOMATIZACIÓN SAKILA")
    print("="*50)
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # PASO 1: Ejecutar proceso ETL
    print("PASO 1: Procesando datos de MySQL...\n")
    if ejecutar_etl():
        print("\n✅ Datos procesados exitosamente!")
        
        # PASO 2: Abrir Excel si está configurado en .env
        if AUTO_OPEN_EXCEL:
            print("\nPASO 2: Abriendo Excel...")
            # Construir ruta absoluta al archivo Excel
            excel_path = Path(__file__).parent / EXCEL_FILE
            if excel_path.exists():
                try:
                    os.startfile(str(excel_path))
                    print(f"✓ Excel abierto: {EXCEL_FILE}")
                    print("\n💡 Para actualizar los datos en Excel:")
                    print("   → Presiona F5")
                    print("   → O: Datos → Actualizar todo")
                    print("   → O: Clic derecho en tabla → Actualizar")
                except Exception as e:
                    print(f"⚠️  No se pudo abrir Excel: {e}")
            else:
                print(f"\n⚠️  Archivo Excel no encontrado: {EXCEL_FILE}")
                print(f"   Crea el archivo en la carpeta 'dashboard/' y vuelve a ejecutar")
                print(f"\n💡 Ver: dashboard/README.md y docs/GUIA_EXCEL.md para instrucciones")
        
        # Resumen final
        print("\n" + "="*50)
        print("✅ PROCESO COMPLETADO")
        print("="*50)
        print(f"\n📂 Archivos generados en '{OUTPUT_FOLDER}/':")
        print("   • datos_sakila.csv")
        print("\n💾 Los datos en formato CSV están listos para Excel")

    else:
        print("\n" + "="*50)
        print("❌ ERROR EN EL PROCESO")
        print("="*50)
        print("\n💡 Posibles causas:")
        print("   1. MySQL no está corriendo")
        print("   2. Credenciales incorrectas en archivo .env")
        print("   3. Base de datos 'sakila' no existe")
        print("\n📖 Ver: README.md sección 'Solución de Problemas'")
        return False
    
    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Proceso interrumpido por el usuario")
    except Exception as e:
        print(f"\n\n❌ Error inesperado: {e}")
        print("📖 Ver: README.md para troubleshooting")
    finally:
        input("\n\nPresiona ENTER para salir...")