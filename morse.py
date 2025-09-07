import sys
import os
from time import sleep

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from morse_audio import play_text_audio, morse_to_audio
    AUDIO_AVAILABLE = True
except ImportError:
    print("Advertencia: Módulo de audio no disponible. La funcionalidad de audio estará deshabilitada.")
    AUDIO_AVAILABLE = False

try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False

COLOR_MAP = {
    'blue': Fore.BLUE,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'red': Fore.RED,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN
}

def print_colored(text, color=None, style=None):
    if not COLORS_AVAILABLE:
        print(text)
        return
    colored_text = text
    if style == 'bright':
        colored_text = Style.BRIGHT + colored_text
    if color and color in COLOR_MAP:
        colored_text = COLOR_MAP[color] + colored_text
    print(colored_text)

def input_colored(prompt, color=None):
    if not COLORS_AVAILABLE:
        return input(prompt)
    if color and color in COLOR_MAP:
        colored_prompt = COLOR_MAP[color] + Style.BRIGHT + prompt + Style.RESET_ALL
    else:
        colored_prompt = prompt
    return input(colored_prompt)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/',
}

TEXT_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encode_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(char, '?') for char in text)

def encode_to_morse_with_audio(text):
    if not AUDIO_AVAILABLE:
        print_colored("Audio no disponible.", 'red')
        return encode_to_morse(text)

    text = text.upper()
    morse_code = [MORSE_CODE_DICT.get(char, '?') if char != ' ' else '/' for char in text]
    morse_string = ' '.join(morse_code)

    print_colored(f"Texto original: {text}", 'yellow')
    print_colored(f"Código Morse: {morse_string}", 'yellow')
    print_colored("Reproduciendo audio completo...", 'yellow')

    try:
        success = play_text_audio(text)
        print_colored("Audio correcto" if success else "Error en audio", 'green' if success else 'red')
    except Exception as e:
        print_colored(f"Error audio: {e}", 'red')

    return morse_string

def decode_from_morse(morse_code):
    words = morse_code.split('/')
    decoded = []
    for word in words:
        letters = word.strip().split()
        decoded_word = ''.join(TEXT_DICT.get(letter, '?') for letter in letters if letter)
        decoded.append(decoded_word)
    return ' '.join(decoded)

def main():
    while True:
        print_colored("\n=== Codificador/Decodificador de Código Morse ===", 'blue', 'bright')
        print_colored("1. Codificar texto a Morse", 'green')
        if AUDIO_AVAILABLE:
            print_colored("2. Codificar texto a Morse (con audio)", 'yellow')
            print_colored("3. Decodificar Morse a texto", 'magenta')
            print_colored("4. Salir", 'red')
            choice = input_colored("\nSelecciona una opción (1-4): ", 'blue')
            max_opt = '4'
        else:
            print_colored("2. Decodificar Morse a texto", 'magenta')
            print_colored("3. Salir (Audio no disponible)", 'red')
            choice = input_colored("\nSelecciona una opción (1-3): ", 'blue')
            max_opt = '3'

        try:
            if choice == '1':
                text = input_colored("Ingresa el texto a codificar: ", 'green')
                result = encode_to_morse(text)
                print_colored(f"Texto original: {text}", 'green')
                print_colored(f"Código Morse: {result}", 'green')
            elif choice == '2' and AUDIO_AVAILABLE:
                text = input_colored("Ingresa el texto a codificar (con audio): ", 'yellow')
                encode_to_morse_with_audio(text)
            elif choice == '2' and not AUDIO_AVAILABLE or choice == '3' and AUDIO_AVAILABLE:
                morse = input_colored("Ingresa el código Morse a decodificar: ", 'magenta')
                result = decode_from_morse(morse)
                print_colored(f"Código Morse: {morse}", 'magenta')
                print_colored(f"Texto decodificado: {result}", 'magenta')
            elif choice == max_opt:
                print_colored("¡Hasta luego!", 'red')
                break
            else:
                print_colored("Opción no válida. Intenta de nuevo.", 'red')
        except KeyboardInterrupt:
            print_colored("Programa interrumpido. ¡Hasta luego!", 'red')
            break
        except Exception as e:
            print_colored(f"Error: {e}", 'red')

if __name__ == "__main__":
    main()
