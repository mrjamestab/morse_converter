#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de audio para código Morse
Genera sonidos usando numpy y scipy
"""

import numpy as np
import scipy.io.wavfile as wav
import tempfile
import os
import time
import platform

# Configuración de audio
SAMPLE_RATE = 44100  # Hz
FREQUENCY_VOWELS = 800    # Hz (frecuencia para vocales)
FREQUENCY_CONSONANTS = 600 # Hz (frecuencia para consonantes)
DOT_DURATION = 0.1   # segundos
DASH_DURATION = 0.3  # segundos
PAUSE_DURATION = 0.1 # segundos entre símbolos
LETTER_PAUSE = 0.2   # segundos entre letras
WORD_PAUSE = 0.7     # segundos entre palabras

# Definir vocales y consonantes
VOWELS = {'A', 'E', 'I', 'O', 'U'}
CONSONANTS = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}

def generate_tone(duration, frequency=FREQUENCY_VOWELS, sample_rate=SAMPLE_RATE):
    """
    Genera un tono sinusoidal
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t)
    # Aplicar envelope para suavizar el inicio y fin
    fade_samples = int(0.01 * sample_rate)  # 10ms fade
    if len(tone) > fade_samples * 2:
        # Fade in
        tone[:fade_samples] *= np.linspace(0, 1, fade_samples)
        # Fade out
        tone[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    return tone

def generate_pause(duration, sample_rate=SAMPLE_RATE):
    """
    Genera un silencio
    """
    return np.zeros(int(sample_rate * duration))

def morse_to_audio(morse_code, original_char=''):
    """
    Convierte código Morse a audio usando frecuencia diferente para vocales/consonantes
    """
    # Determinar la frecuencia basada en si es vocal o consonante
    if original_char.upper() in VOWELS:
        frequency = FREQUENCY_VOWELS
    elif original_char.upper() in CONSONANTS:
        frequency = FREQUENCY_CONSONANTS
    else:
        frequency = FREQUENCY_VOWELS  # frecuencia por defecto

    audio_data = []

    for char in morse_code:
        if char == '.':
            # Punto
            audio_data.append(generate_tone(DOT_DURATION, frequency))
            audio_data.append(generate_pause(PAUSE_DURATION))
        elif char == '-':
            # Línea
            audio_data.append(generate_tone(DASH_DURATION, frequency))
            audio_data.append(generate_pause(PAUSE_DURATION))
        elif char == ' ':
            # Espacio entre letras
            audio_data.append(generate_pause(LETTER_PAUSE))
        elif char == '/':
            # Espacio entre palabras
            audio_data.append(generate_pause(WORD_PAUSE))

    if audio_data:
        # Combinar todos los segmentos de audio
        full_audio = np.concatenate(audio_data)
        # Normalizar para evitar distorsión
        if np.max(np.abs(full_audio)) > 0:
            full_audio = full_audio / np.max(np.abs(full_audio)) * 0.8
        return full_audio
    else:
        return np.array([])

def play_morse_audio(morse_code, original_char=''):
    """
    Reproduce el audio del código Morse usando archivos WAV temporales
    """
    try:
        audio_data = morse_to_audio(morse_code, original_char)

        if len(audio_data) > 0:
            # Crear archivo temporal WAV
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
                temp_filename = temp_file.name

            # Convertir a 16-bit PCM
            audio_int16 = (audio_data * 32767).astype(np.int16)

            # Guardar como WAV
            wav.write(temp_filename, SAMPLE_RATE, audio_int16)

            # Reproducir usando el reproductor predeterminado del sistema
            if platform.system() == 'Windows':
                os.system(f'start /min "" "{temp_filename}"')
            elif platform.system() == 'Darwin':  # macOS
                os.system(f'afplay "{temp_filename}"')
            else:  # Linux
                os.system(f'aplay "{temp_filename}"')

            # Esperar un poco antes de eliminar el archivo
            time.sleep(len(audio_data) / SAMPLE_RATE + 1)
            os.unlink(temp_filename)
            return True
        else:
            print("No hay audio para reproducir")
            return False

    except Exception as e:
        print(f"Error al reproducir audio: {e}")
        return False


def play_text_audio(text):
    """
    Reproduce el audio completo de un texto con frecuencias diferenciadas
    """
    try:
        text = text.upper()
        audio_segments = []

        for char in text:
            if char in VOWELS:
                frequency = FREQUENCY_VOWELS
            elif char in CONSONANTS:
                frequency = FREQUENCY_CONSONANTS
            else:
                frequency = FREQUENCY_VOWELS  # frecuencia por defecto

            if char in MORSE_DICT:
                morse_code = MORSE_DICT[char]
                audio_segments.append(morse_to_audio_with_freq(morse_code, frequency))
                # Agregar pausa entre letras
                audio_segments.append(generate_pause(LETTER_PAUSE))
            elif char == ' ':
                # Agregar pausa entre palabras
                audio_segments.append(generate_pause(WORD_PAUSE))

        if audio_segments:
            # Combinar todos los segmentos
            full_audio = np.concatenate(audio_segments)
            # Normalizar
            if np.max(np.abs(full_audio)) > 0:
                full_audio = full_audio / np.max(np.abs(full_audio)) * 0.8

            # Crear archivo temporal y reproducir
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
                temp_filename = temp_file.name

            audio_int16 = (full_audio * 32767).astype(np.int16)
            wav.write(temp_filename, SAMPLE_RATE, audio_int16)

            if platform.system() == 'Windows':
                os.system(f'start /min "" "{temp_filename}"')
            elif platform.system() == 'Darwin':
                os.system(f'afplay "{temp_filename}"')
            else:
                os.system(f'aplay "{temp_filename}"')

            time.sleep(len(full_audio) / SAMPLE_RATE + 1)
            os.unlink(temp_filename)
            return True
        else:
            return False

    except Exception as e:
        print(f"Error al reproducir audio del texto: {e}")
        return False


def morse_to_audio_with_freq(morse_code, frequency):
    """
    Convierte código Morse a audio usando una frecuencia específica
    """
    audio_data = []

    for char in morse_code:
        if char == '.':
            audio_data.append(generate_tone(DOT_DURATION, frequency))
            audio_data.append(generate_pause(PAUSE_DURATION))
        elif char == '-':
            audio_data.append(generate_tone(DASH_DURATION, frequency))
            audio_data.append(generate_pause(PAUSE_DURATION))

    if audio_data:
        return np.concatenate(audio_data)
    else:
        return np.array([])


# Diccionario de código Morse para el módulo de audio
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}

def text_to_morse_with_audio(text, morse_dict):
    """
    Convierte texto a código Morse y opcionalmente reproduce el audio
    """
    text = text.upper()
    morse_code = []

    for char in text:
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        elif char == ' ':
            morse_code.append('/')
        else:
            morse_code.append('?')  # Carácter desconocido

    return ' '.join(morse_code)

# Función de prueba
def test_audio():
    """
    Función de prueba para verificar que el audio funciona con frecuencias diferenciadas
    """
    print("Probando generación de audio con frecuencias diferenciadas...")
    print(f"Frecuencia vocales: {FREQUENCY_VOWELS} Hz")
    print(f"Frecuencia consonantes: {FREQUENCY_CONSONANTS} Hz")

    # Probar vocales
    print("\n--- Probando vocales ---")
    vowels_morse = ".- .. . --- ..-"  # A I E O U
    print(f"Reproduciendo vocales (A I E O U): {vowels_morse}")
    play_morse_audio(vowels_morse, 'A')
    time.sleep(0.5)
    play_morse_audio("..", 'I')
    time.sleep(0.5)
    play_morse_audio(".", 'E')
    time.sleep(0.5)
    play_morse_audio("---", 'O')
    time.sleep(0.5)
    play_morse_audio("..-", 'U')

    time.sleep(1)

    # Probar consonantes
    print("\n--- Probando consonantes ---")
    consonants_morse = "-... -.-. -.."  # B C D
    print(f"Reproduciendo consonantes (B C D): {consonants_morse}")
    play_morse_audio("-...", 'B')
    time.sleep(0.5)
    play_morse_audio("-.-.", 'C')
    time.sleep(0.5)
    play_morse_audio("-..", 'D')

    time.sleep(1)

    # Probar palabra completa
    print("\n--- Probando palabra completa ---")
    hello_morse = ".... . .-.. .-.. ---"
    print(f"Reproduciendo HELLO: {hello_morse}")
    # Reproducir cada letra con su frecuencia correspondiente
    play_morse_audio("....", 'H')  # H = consonante
    time.sleep(0.3)
    play_morse_audio(".", 'E')     # E = vocal
    time.sleep(0.3)
    play_morse_audio(".-..", 'L') # L = consonante
    time.sleep(0.3)
    play_morse_audio(".-..", 'L') # L = consonante
    time.sleep(0.3)
    play_morse_audio("---", 'O')   # O = vocal

if __name__ == "__main__":
    test_audio()
