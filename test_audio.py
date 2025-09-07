#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para la funcionalidad de audio de código Morse
"""

from morse import encode_to_morse, play_morse_audio

def test_audio():
    """Prueba la reproducción de audio"""
    print("=== Prueba de Reproducción de Audio ===")

    # Prueba con texto simple
    text = "SOS"
    morse = encode_to_morse(text)
    print(f"Texto: {text}")
    print(f"Código Morse: {morse}")
    print("Reproduciendo audio...")

    try:
        play_morse_audio(morse)
        print("✅ Reproducción completada exitosamente")
    except Exception as e:
        print(f"❌ Error en reproducción: {e}")

if __name__ == "__main__":
    test_audio()
