# Codificador/Decodificador de Código Morse

Una aplicación simple en Python para codificar y decodificar texto usando código Morse.

## Características

- ✅ Codificación de texto a código Morse
- ✅ Decodificación de código Morse a texto
- ✅ **Reproducción de audio simultánea** - El código Morse se muestra mientras se reproduce el audio
- ✅ **Frecuencias diferenciadas** - Vocales (800 Hz) vs Consonantes (600 Hz)
- ✅ **Interfaz colorida** - Menú con colores y formato para mejor experiencia visual
- ✅ Soporte para letras, números y espacios
- ✅ Manejo de errores para caracteres desconocidos

## Uso

### Ejecutar la aplicación

```bash
python morse.py
```

### Menú de opciones

1. **Codificar texto a Morse**: Convierte texto normal a código Morse (sin audio)
2. **Codificar texto a Morse (con audio)**: Convierte texto y muestra el código Morse mientras reproduce los sonidos simultáneamente
3. **Decodificar Morse a texto**: Convierte código Morse a texto normal
4. **Salir**: Termina el programa

### Ejemplos

#### Codificación (sin audio):
- Entrada: `HELLO WORLD`
- Salida: `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`

#### Codificación con audio simultáneo:
- Entrada: `HI`
- Salida visual: `.... .. ` (se muestra progresivamente)
- Audio: Se reproduce el sonido correspondiente a cada símbolo mientras se muestra

#### Codificación con audio simultáneo:
```
🔵 === Codificador/Decodificador de Código Morse ===
🟢 1. Codificar texto a Morse
🟡 2. Codificar texto a Morse (con audio)
🟣 3. Decodificar Morse a texto
🔴 4. Salir

🔵 Selecciona una opción (1-4): 2
🟡 Ingresa el texto a codificar (con audio): HOLA
🟡 Texto original: HOLA
🟡 Código Morse: .... --- .-.. .-
🟡 Reproduciendo audio completo...
🟢 Audio reproducido correctamente.
```

### Reproducción de Audio Simultánea

La aplicación puede mostrar el código Morse y reproducir los sonidos al mismo tiempo:

- **Opción 2**: Muestra primero el código Morse completo, luego reproduce los sonidos de cada letra
- **Punto (.)**: Pitido corto (0.1 segundos)
- **Raya (-)**: Pitido largo (0.3 segundos)
- **Pausa entre símbolos**: 0.1 segundos
- **Pausa entre letras**: 0.3 segundos
- **Pausa entre palabras**: 0.7 segundos

**Frecuencias diferenciadas:**
- **Vocales (A, E, I, O, U)**: 800 Hz (tono más agudo)
- **Consonantes (resto de letras)**: 600 Hz (tono más grave)
- **Números y símbolos**: 800 Hz (frecuencia por defecto)

## Interfaz Colorida

La aplicación incluye una interfaz colorida para mejorar la experiencia visual:

- 🔵 **Título**: Azul brillante
- 🟢 **Codificación**: Verde
- 🟡 **Audio**: Amarillo
- 🟣 **Decodificación**: Magenta
- 🔴 **Salir/Errores**: Rojo

Los colores se adaptan automáticamente según la terminal y el sistema operativo.

## Código Morse Soportado

### Letras
- A: .-
- B: -...
- C: -.-.
- D: -..
- E: .
- F: ..-.
- G: --.
- H: ....
- I: ..
- J: .---
- K: -.- 
- L: .-..
- M: --
- N: -.
- O: ---
- P: .--.
- Q: --.-
- R: .-.
- S: ...
- T: -
- U: ..-
- V: ...-
- W: .--
- X: -..-
- Y: -.--
- Z: --..

### Números
- 0: -----
- 1: .----
- 2: ..---
- 3: ...--
- 4: ....-
- 5: .....
- 6: -....
- 7: --...
- 8: ---..
- 9: ----.

### Espacio entre palabras: /

## Pruebas

Para ejecutar las pruebas:

```bash
python test_morse.py
```

## Requisitos

- Python 3.6+
- numpy (para generación de tonos de audio)
- scipy (para reproducción de audio)
- colorama (para colores en terminal)
- Entorno virtual (venv) configurado

## Instalación

1. Clona o descarga los archivos
2. Configura el entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instala las dependencias:
   ```bash
   pip install numpy scipy colorama
   ```

## Estructura del Proyecto

```
morse/
├── morse.py          # Aplicación principal
├── morse_audio.py    # Módulo de audio para reproducción de sonidos
├── test_morse.py     # Script de pruebas
├── test_audio.py     # Script de pruebas de audio
├── temp_tone.wav     # Archivo temporal de audio
├── venv/             # Entorno virtual
├── __pycache__/      # Archivos compilados de Python
└── README.md         # Este archivo
```

## Contribuciones

Si encuentras errores o quieres mejorar la aplicación, ¡las contribuciones son bienvenidas!</content>
<parameter name="filePath">d:\DEVS\morse\README.md
