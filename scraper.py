import requests
import json
import urllib3

urllib3.disable_warnings()

url = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

print("Descargando datos del Ministerio...")
try:
    r = requests.get(url, headers=headers, verify=False, timeout=60)
    r.raise_for_status() # Lanza error si no es 200
    
    # Guardamos los datos en un archivo JSON
    with open('datos.json', 'w', encoding='utf-8') as f:
        json.dump(r.json(), f, ensure_ascii=False)
        
    print("✅ Datos guardados correctamente en datos.json")
except Exception as e:
    print(f"❌ Error al descargar: {e}")
    exit(1)
