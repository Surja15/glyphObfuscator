# 🔐 Text Obfuscation Tool

A simple yet effective **text/code obfuscation tool** written in Python. This project replaces ASCII characters with visually similar **Unicode homoglyphs** to make code or text harder to read by automated systems (e.g., scanners, parsers, or malware detection tools), while still appearing visually similar to humans.

## 💡 Use Case

This tool is designed for **cybersecurity research**, red teaming, or educational purposes to demonstrate:
- **Homoglyph attacks** / text obfuscation techniques
- How malware or phishing attempts may evade basic text-based filters
- Unicode misuse in source code to bypass detection

⚠️ **Disclaimer**: This tool is for educational purposes only. Do not use it for malicious activities.

---

## 🔧 Features

- Obfuscates (encodes) or de-obfuscates (decodes) entire blocks of text or code.
- Supports:
  - Manual input via terminal
  - File input from `.txt` files
- Saves output to `encrypted.txt` or `decrypted.txt`

---

## 🧠 How It Works

This script uses a custom mapping (`obfuscation_map`) to replace standard English alphabet characters with their **Unicode homoglyph equivalents** — characters from other scripts (Greek, Cyrillic, Armenian, etc.) that visually resemble ASCII letters but have different underlying code points.

Example:
```text
Original   : print("Hello World")
Obfuscated : ргіոт("Ηеⅼⅼο Ԝοгⅼԁ")

🚀 Usage
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/unicode-obfuscator.git
cd unicode-obfuscator
Run the script:

bash
Copy
Edit
python obfuscator.py
Follow the menu prompts:

Choose to encrypt or decrypt

Choose to input raw text or use a file

Output will be saved in a .txt file

📁 File Structure
pgsql
Copy
Edit
.
├── obfuscator.py        # Main script
├── encrypted.txt        # Output file for obfuscated text (generated)
├── decrypted.txt        # Output file for de-obfuscated text (generated)
🔐 Security Relevance
This tool demonstrates a Unicode obfuscation technique used in:

Phishing URLs

Source code tampering (esp. open-source supply chain attacks)

Email bypass attempts

Obfuscated malware payloads

It highlights the importance of:

Normalizing inputs in software

Unicode-aware security scanning

Defending against visual spoofing and symbol confusion

📜 License
MIT License

👨‍💻 Author
Surja15

