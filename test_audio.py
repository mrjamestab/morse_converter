from morse import encode_to_morse
from morse_audio import play_morse_audio

def test_audio():
    print("Audio test:")
    text = "SOS"
    morse = encode_to_morse(text)
    print(f"Text: {text}")
    print(f"Morse: {morse}")
    print("Playing audio...")
    try:
        success = play_morse_audio(morse)
        print("✅ Success" if success else "❌ Failed")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_audio()
