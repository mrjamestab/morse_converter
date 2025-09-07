import numpy as np
import scipy.io.wavfile as wav
import tempfile
import os
import time
import platform

SAMPLE_RATE = 44100
FREQUENCY_VOWELS = 800
FREQUENCY_CONSONANTS = 600
DOT_DURATION = 0.1
DASH_DURATION = 0.3
PAUSE_DURATION = 0.1
LETTER_PAUSE = 0.2
WORD_PAUSE = 0.7

VOWELS = {'A', 'E', 'I', 'O', 'U'}
CONSONANTS = {'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}

def generate_tone(duration, frequency=FREQUENCY_VOWELS, sample_rate=SAMPLE_RATE):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t)
    fade_samples = int(0.01 * sample_rate)
    if len(tone) > fade_samples * 2:
        tone[:fade_samples] *= np.linspace(0, 1, fade_samples)
        tone[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    return tone

def generate_pause(duration, sample_rate=SAMPLE_RATE):
    return np.zeros(int(sample_rate * duration))

def morse_to_audio(morse_code, original_char=''):
    frequency = FREQUENCY_VOWELS if original_char.upper() in VOWELS else FREQUENCY_CONSONANTS
    audio_data = []
    for char in morse_code:
        if char == '.':
            audio_data.extend([generate_tone(DOT_DURATION, frequency), generate_pause(PAUSE_DURATION)])
        elif char == '-':
            audio_data.extend([generate_tone(DASH_DURATION, frequency), generate_pause(PAUSE_DURATION)])
        elif char == ' ':
            audio_data.append(generate_pause(LETTER_PAUSE))
        elif char == '/':
            audio_data.append(generate_pause(WORD_PAUSE))
    if audio_data:
        full_audio = np.concatenate(audio_data)
        max_val = np.max(np.abs(full_audio))
        return full_audio / max_val * 0.8 if max_val > 0 else full_audio
    return np.array([])

def play_morse_audio(morse_code, original_char=''):
    try:
        audio_data = morse_to_audio(morse_code, original_char)
        if len(audio_data) == 0:
            return False
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
            temp_file = f.name
        wav.write(temp_file, SAMPLE_RATE, (audio_data * 32767).astype(np.int16))
        cmd = {'Windows': f'start /min "" "{temp_file}"', 'Darwin': f'afplay "{temp_file}"'}.get(platform.system(), f'aplay "{temp_file}"')
        os.system(cmd)
        time.sleep(len(audio_data) / SAMPLE_RATE + 1)
        os.unlink(temp_file)
        return True
    except Exception as e:
        print(f"Audio error: {e}")
        return False

def play_text_audio(text):
    try:
        text = text.upper()
        audio_segments = []
        for char in text:
            freq = FREQUENCY_VOWELS if char in VOWELS else FREQUENCY_CONSONANTS
            if char in MORSE_DICT:
                audio_segments.extend([morse_to_audio_with_freq(MORSE_DICT[char], freq), generate_pause(LETTER_PAUSE)])
            elif char == ' ':
                audio_segments.append(generate_pause(WORD_PAUSE))
        if not audio_segments:
            return False
        full_audio = np.concatenate(audio_segments)
        max_val = np.max(np.abs(full_audio))
        if max_val > 0:
            full_audio /= max_val
            full_audio *= 0.8
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f:
            temp_file = f.name
        wav.write(temp_file, SAMPLE_RATE, (full_audio * 32767).astype(np.int16))
        cmd = {'Windows': f'start /min "" "{temp_file}"', 'Darwin': f'afplay "{temp_file}"'}.get(platform.system(), f'aplay "{temp_file}"')
        os.system(cmd)
        time.sleep(len(full_audio) / SAMPLE_RATE + 1)
        os.unlink(temp_file)
        return True
    except Exception as e:
        print(f"Audio error: {e}")
        return False

def morse_to_audio_with_freq(morse_code, frequency):
    audio_data = []
    for char in morse_code:
        if char == '.':
            audio_data.extend([generate_tone(DOT_DURATION, frequency), generate_pause(PAUSE_DURATION)])
        elif char == '-':
            audio_data.extend([generate_tone(DASH_DURATION, frequency), generate_pause(PAUSE_DURATION)])
    return np.concatenate(audio_data) if audio_data else np.array([])

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
