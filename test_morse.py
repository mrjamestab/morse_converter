#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para las funciones de código Morse
"""

from morse import encode_to_morse, decode_from_morse

def test_encoding():
    """Prueba la función de codificación"""
    print("=== Pruebas de Codificación ===")

    test_cases = [
        ("HELLO", ".... . .-.. .-.. ---"),
        ("WORLD", ".-- --- .-. .-.. -.."),
        ("SOS", "... --- ..."),
        ("123", ".---- ..--- ...--"),
        ("HI!", ".... .. ?"),
    ]

    for text, expected in test_cases:
        result = encode_to_morse(text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{text}' -> '{result}'")
        if result != expected:
            print(f"   Esperado: '{expected}'")

def test_decoding():
    """Prueba la función de decodificación"""
    print("\n=== Pruebas de Decodificación ===")

    test_cases = [
        (".... . .-.. .-.. ---", "HELLO"),
        (".-- --- .-. .-.. -..", "WORLD"),
        ("... --- ...", "SOS"),
        (".---- ..--- ...--", "123"),
        (".... .. ?????.", "HI?"),
    ]

    for morse, expected in test_cases:
        result = decode_from_morse(morse)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{morse}' -> '{result}'")
        if result != expected:
            print(f"   Esperado: '{expected}'")

def test_round_trip():
    """Prueba ida y vuelta: texto -> morse -> texto"""
    print("\n=== Pruebas de Ida y Vuelta ===")

    test_texts = [
        "HELLO WORLD",
        "SOS",
        "PYTHON",
        "123 ABC",
    ]

    for text in test_texts:
        morse = encode_to_morse(text)
        decoded = decode_from_morse(morse)
        status = "✓" if decoded == text else "✗"
        print(f"{status} '{text}' -> '{morse}' -> '{decoded}'")

if __name__ == "__main__":
    test_encoding()
    test_decoding()
    test_round_trip()
    print("\n=== Pruebas completadas ===")
