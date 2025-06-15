obfuscation_map = {
    # My custom map, the characters look similar to their ASCII counterparts but are not the same:
    'A': 'Α', 'B': 'Β', 'C': 'Ϲ', 'D': 'Ɗ', 'E': 'Ε', 'F': 'Ϝ', 'G': 'ɢ',
    'H': 'Η', 'I': 'Ι', 'J': 'Ј', 'K': 'Κ', 'L': 'ʟ', 'M': 'Μ', 'N': 'Ν',
    'O': 'Ο', 'P': 'Ρ', 'Q': 'Ⴓ', 'R': 'Ʀ', 'S': 'Ѕ', 'T': 'Τ', 'U': 'Ս',
    'V': 'Ѵ', 'W': 'Ԝ', 'X': 'Χ', 'Y': 'Υ', 'Z': 'Ζ',
    'a': 'α', 'b': 'ь', 'c': 'ϲ', 'd': 'ժ', 'e': 'е', 'f': 'ғ', 'g': 'ɡ',
    'h': 'һ', 'i': 'і', 'j': 'ʝ', 'k': 'κ', 'l': 'ⅼ', 'm': 'м', 'n': 'ո',
    'o': 'ο', 'p': 'ρ', 'q': 'զ', 'r': 'г', 's': 'ѕ', 't': 'т', 'u': 'υ',
    'v': 'ⅴ', 'w': 'ѡ', 'x': 'х', 'y': 'у', 'z': 'ᴢ'
}

reverse_map = {v: k for k, v in obfuscation_map.items()}

def encode_char(ch):
    return obfuscation_map.get(ch, ch)

def decode_char(ch):
    return reverse_map.get(ch, ch)

def process_text(text, mode='encode'):
    func = encode_char if mode == 'encode' else decode_char
    return ''.join(func(ch) for ch in text)

def get_raw_input():
    print("Paste your text/code now. Type a single '.' on a new line when done:")
    lines = []
    while True:
        line = input()
        if line.strip() == '.':
            break
        lines.append(line)
    return '\n'.join(lines)

def get_file_input():
    while True:
        filepath = input("Enter full path to the input .txt file: ").strip()
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading file: {e}. Please try again.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '3':
            print("Exiting...")
            break
        elif choice not in ('1', '2'):
            print("Invalid choice. Try again.")
            continue

        print("\nChoose input method:")
        print("1. Input raw text/code")
        print("2. Read from .txt file")
        input_method = input("Enter 1 or 2: ").strip()

        if input_method == '1':
            raw_text = get_raw_input()
        elif input_method == '2':
            raw_text = get_file_input()
        else:
            print("Invalid input method choice. Returning to main menu.")
            continue

        if choice == '1':
            output_text = process_text(raw_text, 'encode')
            output_file = 'encrypted.txt'
        else:
            output_text = process_text(raw_text, 'decode')
            output_file = 'decrypted.txt'

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output_text)

        print(f"\nOutput written to {output_file}")

if __name__ == "__main__":
    main()
