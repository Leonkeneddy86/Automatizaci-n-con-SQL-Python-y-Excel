# 🚀 Automatización con SQL, Python y Excel

## 🎯 Descripción del Proyecto

Este proyecto implementa un **pipeline ETL (Extraer, Transformar, Cargar)** utilizando **Python** para automatizar la extracción de datos de una base de datos **SQL** (por ejemplo, Sakila) y generar reportes analíticos de forma automática.

El proceso automatiza las siguientes salidas:

1. 💾 Un archivo **CSV** (generado a partir de `CSV_PATH`) que contiene datos de transacciones **agregados por cliente** (ingresos totales, número de alquileres, promedio de pago, etc.).
2. 📊 Un archivo **Excel** (`dashboard.xlsx`) que sirve como reporte final, estructurado en tres hojas:

   * **Datos:** Resumen principal por cliente.
   * **Tablas dinámicas:** Resúmenes por país y ciudad.
   * **Dashboard:** Resumen ejecutivo con métricas clave y un **gráfico de barras** (`openpyxl`) del Top 10 de países por ingresos.

---

## 🏗️ Estructura del Proyecto

Estructura de archivos y carpetas:

```
.
├── main.py
├── requirements.txt
├── .env.example
├── output/
└── src/
    ├── __init__.py
    ├── sakila_ETL.py
    └── config.py
```

| Archivo/Carpeta     | Función Principal                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `main.py`           | Punto de entrada que ejecuta el pipeline ETL completo.                                                           |
| `src/sakila_ETL.py` | Lógica de conexión, extracción SQL, transformación de datos (`pandas`) y generación de archivos (`csv`, `xlsx`). |
| `src/config.py`     | Configuración que lee las variables de entorno para la conexión a la base de datos y rutas de salida.            |
| `.env.example`      | Plantilla de variables de entorno necesarias (credenciales de la base de datos).                                 |
| `requirements.txt`  | Lista de dependencias de Python para instalación rápida.                                                         |

---

## ⚙️ Configuración e Instalación

### 1. Requisitos Previos

* **Python 3.x**
* Base de datos SQL disponible (ej. PostgreSQL o MySQL con esquema Sakila)

---

### 2. Clonación del Repositorio

```bash
git clone https://github.com/Leonkeneddy86/Automatizaci-n-con-SQL-Python-y-Excel
cd Automatizaci-n-con-SQL-Python-y-Excel
```

---

### 3. Crear y Activar un Entorno Virtual

Es recomendable trabajar en un entorno virtual para aislar las dependencias. Usaremos `.venv` como nombre del entorno.

#### 3.1 Creación del Entorno

```bash
python -m venv .venv
```

#### 3.2 Activación y Desactivación por Sistema Operativo

| Sistema Operativo / Terminal | Activar Entorno                                      | Desactivar Entorno |
| ---------------------------- | ---------------------------------------------------- | ------------------ |
| Windows (PowerShell)         | `.venv\Scripts\Activate.ps1`                       | `deactivate`       |
| Windows (CMD)                | `.venv\Scripts\activate.bat`                       | `deactivate`       |
| Linux / macOS (Bash/Zsh)     | `source .venv/Scripts/activate`                    | `deactivate`       |

⚠️ **Nota para PowerShell en Windows:** Si aparece un error de ejecución de scripts, ejecuta solo la primera vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### 4. Instalación de Dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

---

### 5. Configuración de Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con tus credenciales de base de datos:

```env
# Usuario de la base de datos
DB_USER=tu_usuario

# Contraseña de la base de datos
DB_PASSWORD=tu_contraseña_segura

# Host de la base de datos
DB_HOST=localhost o 127.0.0.1

# Puerto de la base de datos
DB_PORT=3306

# Nombre de la base de datos
DB_NAME=sakila
```

---

## ▶️ Uso

Para iniciar el pipeline ETL, asegúrate de que tu entorno virtual esté activado y ejecuta:

```bash
python main.py
```

### Resultados

Al finalizar la ejecución, el script generará:

* **Archivo CSV:** Datos agregados por cliente.
* **Archivo Excel (`dashboard.xlsx`):** Reporte con análisis y gráfico de barras.

---

## 💻 Tecnologías Clave

* **Python 3.x**
* **SQLAlchemy:** Conexión eficiente a la base de datos SQL.
* **Pandas:** Manipulación y transformación de DataFrames.
* **OpenPyXL:** Creación avanzada de archivos Excel y gráficos de barras.
* **python-dotenv:** Gestión segura de credenciales de conexión.

---

## 🤝 Colaboradores

| Nombre     | Rol                        | GitHub                                             |
|-----------|----------------------------|--------------------------------------------------|
| Joaquin   | Backend, Python y SQL       | [JoaquinMorenoFernandez](https://github.com/JoaquinMorenoFernandez) |
| Natalia   | Excel y Tablas Dinámicas    | [nataliajoanna](https://github.com/nataliajoanna) |
| Jonathan  | Documentación (README)      | [Leonkeneddy86](https://github.com/Leonkeneddy86) |
