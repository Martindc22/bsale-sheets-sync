import json
import os
import pandas as pd
from datetime import datetime
import gspread

def cargar_datos_bsale():
    """Simula la extracción desde la API REST de Bsale"""
    try:
        with open("mock_bsale_api.json", "r", encoding="utf-8-sig") as file:
            data = json.load(file)
        print("✅ Datos extraídos correctamente de la API Bsale.")
        return data
    except Exception as e:
        print(f"❌ Error al conectar con la API de Bsale: {e}")
        return None

def procesar_y_limpiar_ventas(data_json):
    """Limpia los datos de ventas y elimina duplicados"""
    if not data_json or "ventas" not in data_json:
        return None

    df_ventas = pd.DataFrame(data_json["ventas"])

    # Control de integridad: Evitar registros duplicados por comprobante
    df_ventas.drop_duplicates(subset=["comprobante"], keep="last", inplace=True)
    
    # Timestamp de última sincronización
    df_ventas["fecha_sincronizacion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return df_ventas

def enviar_a_google_sheets(df):
    """Envía el DataFrame procesado a una planilla real de Google Sheets"""
    try:
        # Autenticación mediante Service Account
        gc = gspread.service_account(filename="credentials.json")
        sheet = gc.open("Reporte Ventas Bsale").sheet1
        
        # Preparación de datos (encabezados + filas)
        datos = [df.columns.values.tolist()] + df.values.tolist()
        
        sheet.clear()
        sheet.update("A1", datos)
        print("✅ Datos sincronizados correctamente en Google Sheets.")
    except Exception as e:
        print(f"⚠️ Nota de Google Sheets: {e}")

def sincronizar_sistema():
    print("🔄 Iniciando proceso de sincronización diaria...")
    data = cargar_datos_bsale()

    if data:
        df_ventas = procesar_y_limpiar_ventas(data)
        
        # 1. Guardado en CSV de respaldo local
        archivo_salida = "Sincronizacion_GoogleSheets_Simulada.csv"
        df_ventas.to_csv(archivo_salida, index=False, encoding="utf-8-sig")

        print("\n📊 DATOS PROCESADOS:")
        print(df_ventas.to_string(index=False))
        print(f"\n✅ Respaldo local guardado en '{archivo_salida}'.")

        # 2. Envío a la API de Google Sheets
        enviar_a_google_sheets(df_ventas)

if __name__ == "__main__":
    sincronizar_sistema()
