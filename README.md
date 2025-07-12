
CipherX – Modular Python Encryption Suite

CipherX is a modular, user-friendly encryption & decryption application built with PyQt5.
It supports both classical and modern cryptography algorithms – including Caesar, RSA, and AES – all accessible through a stylish graphical interface.
CipherX is designed for education, experimentation, and as a showcase for secure message handling in Python.

---

🚀 Features

- Multiple encryption algorithms: Caesar cipher (with Turkish support), RSA (public/private key), and AES (symmetric key)
- Modern PyQt5 GUI: Clean, intuitive interface with theme support and advanced user interactions
- Modular codebase: All cipher logic, Excel logging, and styling in separate, well-documented modules
- Automatic key generation and management
- Excel log recording: Encrypted/decrypted messages and keys are saved for audit or recovery
- Detailed error handling and user feedback
- Open for educational use, demos, or rapid prototyping

---

📁 File Structure

CipherX/
├── main.py               # Application entry point
├── main_window.py        # PyQt5 GUI class (window design, signals)
├── styles.py             # GUI style and theme definitions
├── cipher_functions.py   # All encryption/decryption algorithms (Caesar, RSA, AES)
├── excel_functions.py    # Excel logging (logs encrypted/decrypted messages)
├── README.md             # Project documentation
└── [Excel log files]     # Auto-generated logs (not tracked by Git)

---

🛠️ Example Usage

- Encrypt a message:
    1. Launch the app (`python main.py`)
    2. Select an algorithm (Caesar, RSA, AES)
    3. Enter your message and (if required) a key
    4. Click "Encrypt" to get the cipher text, which is also logged automatically

- Decrypt a message:
    1. Paste your encrypted text, enter/select key (if needed)
    2. Click "Decrypt" to reveal the original message

- Auto Key Generation:
    - For AES & RSA, you can generate keys with one click from the interface.

---

📝 License

Open-source for educational and demonstration use.
Not for use in production or critical security contexts.

---

👨‍💻 Author

Developed by Doğukan Avcı
- Email: hulavci121@gmail.com
- GitHub: https://github.com/AvciDogukan
- LinkedIn: https://www.linkedin.com/in/doğukanavcı-119541229/

For feedback or collaboration, feel free to contact!
