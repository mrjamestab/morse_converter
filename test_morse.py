from morse import encode_to_morse, decode_from_morse

def test_encoding():
    print("Encoding tests:")
    cases = [
        ("HELLO", ".... . .-.. .-.. ---"),
        ("WORLD", ".-- --- .-. .-.. -.."),
        ("SOS", "... --- ..."),
        ("123", ".---- ..--- ...--"),
        ("HI!", ".... .. ?"),
    ]
    for text, expected in cases:
        result = encode_to_morse(text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{text}' -> '{result}'")
        if result != expected:
            print(f"Expected: '{expected}'")

def test_decoding():
    print("\nDecoding tests:")
    cases = [
        (".... . .-.. .-.. ---", "HELLO"),
        (".-- --- .-. .-.. -..", "WORLD"),
        ("... --- ...", "SOS"),
        (".---- ..--- ...--", "123"),
        (".... .. ?????.", "HI?"),
    ]
    for morse, expected in cases:
        result = decode_from_morse(morse)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{morse}' -> '{result}'")
        if result != expected:
            print(f"Expected: '{expected}'")

def test_round_trip():
    print("\nRound-trip tests:")
    texts = ["HELLO WORLD", "SOS", "PYTHON", "123 ABC"]
    for text in texts:
        morse = encode_to_morse(text)
        decoded = decode_from_morse(morse)
        status = "✓" if decoded == text else "✗"
        print(f"{status} '{text}' -> '{morse}' -> '{decoded}'")

if __name__ == "__main__":
    test_encoding()
    test_decoding()
    test_round_trip()
    print("\nTests completed.")
