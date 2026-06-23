import asyncio
import edge_tts
import csv
import os

async def procesar_fila(index, texto, carpeta):
    voz = "es-MX-JorgeNeural" # Voces: (DaliaNeural, JorgeNeural)

    # El index :03d hace que se vea como 001, 002, etc.
    nombre_archivo = os.path.join(carpeta, f"dialogo_{index:03d}.mp3")
    try:
        communicate = edge_tts.Communicate(texto, voz)
        await communicate.save(nombre_archivo)
        print(f"✅ Generado: {nombre_archivo}")
    except Exception as e:
        print(f"❌ Error en fila {index}: {e}")

async def main():
    archivo_csv = "dialogos.csv"
    carpeta_salida = "audios_exportados"
    
    if not os.path.exists(archivo_csv):
        print(f"Error: No existe el archivo {archivo_csv}")
        return

    os.makedirs(carpeta_salida, exist_ok=True)
    tareas = []

    with open(archivo_csv, mode='r', encoding='utf-8') as f:
        # Usamos ';' o ':' para evitar el conflicto con las comas del diálogo. Lo usamos donde dice delimiter=
        lector = csv.DictReader(f, delimiter=';') 
        
        for i, fila in enumerate(lector, start=1):
            texto = fila.get("dialogos", "")
            if texto and texto.strip():
                tareas.append(procesar_fila(i, texto, carpeta_salida))

    if tareas:
        print(f"Iniciando descarga masiva de {len(tareas)} audios...")
        await asyncio.gather(*tareas)
        print(f"\n--- ¡Listo! Audios guardados en '{carpeta_salida}' ---")
    else:
        print("No se encontraron diálogos. Revisa que la cabecera del archivo diga 'dialogos'.")

if __name__ == "__main__":
    asyncio.run(main())