## Script voz_ia

Script de Python (version 3.9) para generar audios desde un archivo .CSV (dialogos.csv).
Al ejecutar el script creará un audio por cada fila del archivo dialogo.csv usando 
el servicio de síntesis de voz de Microsoft Edge (EDGE TTS).

### Antes de ejecutar el script debes:

* Instalar Python 3.9.* y tener instalado pip
* instalar la libreria edge-tts desde la consola con el comando: **pip install edge-tts**
* Abrir archivo **dialogo.csv** y escribir lo que quieras que se transforme en audio 
    (el texto debe ser escrito como filas por debajo del titulo "dialogos"). 