# Morse Code Encoder/Decoder
# Importaciones necesarias
import sys
import os
from time import sleep

# Agregar el directorio actual al path para importar morse_audio
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from morse_audio import play_morse_audio as play_audio, play_text_audio, text_to_morse_with_audio
    AUDIO_AVAILABLE = True
except ImportError:
    print("Advertencia: Módulo de audio no disponible. La funcionalidad de audio estará deshabilitada.")
    AUDIO_AVAILABLE = False

# Importar colorama para colores en terminal
try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False

# Funciones auxiliares para colores
def print_colored(text, color=None, style=None):
    """Imprime texto con color si está disponible"""
    if not COLORS_AVAILABLE:
        print(text)
        return

    colored_text = text
    if style == 'bright':
        colored_text = Style.BRIGHT + colored_text
    if color:
        if color == 'blue':
            colored_text = Fore.BLUE + colored_text
        elif color == 'green':
            colored_text = Fore.GREEN + colored_text
        elif color == 'yellow':
            colored_text = Fore.YELLOW + colored_text
        elif color == 'red':
            colored_text = Fore.RED + colored_text
        elif color == 'magenta':
            colored_text = Fore.MAGENTA + colored_text
        elif color == 'cyan':
            colored_text = Fore.CYAN + colored_text

    print(colored_text)

def input_colored(prompt, color=None):
    """Solicita entrada con color si está disponible"""
    if not COLORS_AVAILABLE:
        return input(prompt)

    colored_prompt = prompt
    if color:
        if color == 'blue':
            colored_prompt = Fore.BLUE + Style.BRIGHT + prompt + Style.RESET_ALL
        elif color == 'green':
            colored_prompt = Fore.GREEN + Style.BRIGHT + prompt + Style.RESET_ALL
        elif color == 'yellow':
            colored_prompt = Fore.YELLOW + Style.BRIGHT + prompt + Style.RESET_ALL
        elif color == 'red':
            colored_prompt = Fore.RED + Style.BRIGHT + prompt + Style.RESET_ALL
        elif color == 'magenta':
            colored_prompt = Fore.MAGENTA + Style.BRIGHT + prompt + Style.RESET_ALL
        elif color == 'cyan':
            colored_prompt = Fore.CYAN + Style.BRIGHT + prompt + Style.RESET_ALL

    return input(colored_prompt)

# Diccionario de código Morse
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/',  # Espacio entre palabras
}

# Diccionario inverso para decodificación
TEXT_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def encode_to_morse(text):
    """
    Convierte texto a código Morse
    """
    text = text.upper()
    morse_code = []

    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # Carácter desconocido

    return ' '.join(morse_code)


def encode_to_morse_with_audio(text):
    """
    Convierte texto a código Morse y reproduce audio simultáneamente
    con frecuencias diferentes para vocales y consonantes
    """
    if not AUDIO_AVAILABLE:
        print_colored("La funcionalidad de audio no está disponible.", 'red')
        return encode_to_morse(text)

    text = text.upper()
    morse_code = []

    # Primero construir todo el código Morse
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        elif char == ' ':
            morse_code.append('/')
        else:
            morse_code.append('?')

    morse_string = ' '.join(morse_code)

    # Mostrar el resultado completo
    print_colored(f"Texto original: {text}", 'yellow')
    print_colored(f"Código Morse: {morse_string}", 'yellow')

    # Reproducir el audio completo de todo el texto
    print_colored("Reproduciendo audio completo...", 'yellow')
    try:
        success = play_text_audio(text)
        if success:
            print_colored("Audio reproducido correctamente.", 'green')
        else:
            print_colored("Error al reproducir el audio.", 'red')
    except Exception as e:
        print_colored(f"Error reproduciendo audio: {e}", 'red')

    return morse_string


def decode_from_morse(morse_code):
    """
    Convierte código Morse a texto
    """
    words = morse_code.split('/')
    decoded_text = []

    for word in words:
        letters = word.strip().split(' ')
        decoded_word = []

        for letter in letters:
            if letter in TEXT_DICT:
                decoded_word.append(TEXT_DICT[letter])
            elif letter == '':
                continue
            else:
                decoded_word.append('?')  # Código desconocido

        decoded_text.append(''.join(decoded_word))

    return ' '.join(decoded_text)


def main():
    """
    Función principal del programa
    """
    while True:
        # Título en negrita y color azul
        print_colored("\n=== Codificador/Decodificador de Código Morse ===", 'blue', 'bright')
        print_colored("1. Codificar texto a Morse", 'green')
        if AUDIO_AVAILABLE:
            print_colored("2. Codificar texto a Morse (con audio)", 'yellow')
            print_colored("3. Decodificar Morse a texto", 'magenta')
            print_colored("4. Salir", 'red')
        else:
            print_colored("2. Decodificar Morse a texto", 'magenta')
            print_colored("3. Salir (Audio no disponible)", 'red')

        try:
            if AUDIO_AVAILABLE:
                choice = input_colored("\nSelecciona una opción (1-4): ", 'blue')
                max_option = '4'
            else:
                choice = input_colored("\nSelecciona una opción (1-3): ", 'blue')
                max_option = '3'

            if choice == '1':
                text = input_colored("Ingresa el texto a codificar: ", 'green')
                result = encode_to_morse(text)
                print_colored(f"Texto original: {text}", 'green')
                print_colored(f"Código Morse: {result}", 'green')

            elif choice == '2' and AUDIO_AVAILABLE:
                text = input_colored("Ingresa el texto a codificar (con audio): ", 'yellow')
                result = encode_to_morse_with_audio(text)

            elif choice == '2' and not AUDIO_AVAILABLE:
                morse = input_colored("Ingresa el código Morse a decodificar: ", 'magenta')
                result = decode_from_morse(morse)
                print_colored(f"Código Morse: {morse}", 'magenta')
                print_colored(f"Texto decodificado: {result}", 'magenta')

            elif choice == '3' and AUDIO_AVAILABLE:
                morse = input_colored("Ingresa el código Morse a decodificar: ", 'magenta')
                result = decode_from_morse(morse)
                print_colored(f"Código Morse: {morse}", 'magenta')
                print_colored(f"Texto decodificado: {result}", 'magenta')

            elif choice == '4' and AUDIO_AVAILABLE:
                print_colored("¡Hasta luego!", 'red')
                break

            elif choice == '3' and not AUDIO_AVAILABLE:
                print_colored("¡Hasta luego!", 'red')
                break

            else:
                print_colored("Opción no válida. Intenta de nuevo.", 'red')

        except KeyboardInterrupt:
            print_colored("\n\nPrograma interrumpido. ¡Hasta luego!", 'red')
            break
        except Exception as e:
            print_colored(f"Error: {e}", 'red')


if __name__ == "__main__":
    main()
