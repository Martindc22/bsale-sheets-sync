# 🔄 Bsale API ➔ Google Sheets Sync (ETL Pipeline)

Script automatizado en Python para extraer, transformar e integrar datos de ventas y stock desde la API REST de **Bsale** hacia **Google Sheets**.

## 🎯 Características Principales
- **Consumo API REST:** Extracción de datos en formato JSON desde los endpoints de Bsale.
- **Control de Integridad:** Prevención de duplicados mediante filtrado único por comprobante/ID.
- **Auditoría:** Registro automático de la última fecha y hora de sincronización (timestamp).
- **Respaldo Local:** Exportación de backup de seguridad en CSV.
- **Resiliencia:** Manejo robusto de errores (try/except) para proteger la ejecución ante caídas de red o credenciales inválidas.

## 🛠️ Tecnologías Utilizadas
- **Python 3.12+**
- **Pandas** (Procesamiento y limpieza de datos)
- **gspread** (Integración oficial con la API de Google Sheets)
- **Requests** (Consumo de API REST)

## 🚀 Instrucciones de Configuración y Ejecución

1. Clonar el repositorio:
   git clone https://github.com/Martindc22/bsale-sheets-sync.git
   cd bsale-sheets-sync

2. Instalar dependencias:
   pip install -r requirements.txt

3. Ejecutar la sincronización:
   python main_sync.py
