# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:49:25 2024

@author: Dogukan Avcı

Main Windows
"""

# main_window.py
import random
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
from cipher_functions import encrypt, decrypt, generate_id, characters, rsa_encrypt, rsa_decrypt, generate_rsa_keys, aes_encrypt, aes_decrypt, generate_aes_key
from excel_functions import log_to_excel, open_excel_file

class CipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('CipherX - Şifreleme Uygulaması')
        self.setGeometry(100, 100, 800, 600)

        # Temayı ayarlayın
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(224, 229, 236))  # Body background color
        self.setPalette(palette)

        # Font ayarları
        font = QFont("Helvetica", 14)
        font.setBold(True)
        font.setPointSize(12)
        
        label_font = QFont("Cormorant Garamond", 50)
        label_font.setBold(False)
        
        button_font = QFont("Helvetica", 12)
        button_font.setBold(True)
        
        # Karşılama ekranı
        self.welcome_screen = QWidget(self)
        welcome_layout = QVBoxLayout()
        
        welcome_label = QLabel('Merhaba! CipherX Uygulamasına Hoşgeldiniz', self.welcome_screen)
        welcome_label.setFont(label_font)
        welcome_label.setAlignment(Qt.AlignCenter)
        
        welcome_button = QPushButton('Başlamak İçin Tıklayın', self.welcome_screen)
        welcome_button.setFont(button_font)
        welcome_button.setObjectName("welcomeButton")  # Stil için id belirledik
        welcome_button.clicked.connect(self.show_cipher_screen)
        
        welcome_layout.addWidget(welcome_label)
        welcome_layout.addWidget(welcome_button)
        self.welcome_screen.setLayout(welcome_layout)
        
        # Şifreleme ekranı
        self.cipher_screen = QWidget(self)
        cipher_layout = QVBoxLayout(self.cipher_screen)

        self.version_label = QLabel('Versiyon: 1.0.0', self.cipher_screen)
        self.version_label.setFont(font)

        self.message_label = QLabel('Mesaj:', self.cipher_screen)
        self.message_label.setFont(font)
        
        self.message_input = QLineEdit(self.cipher_screen)
        self.message_input.setFont(font)

        self.key_label = QLabel('Anahtar (ID veya Key):', self.cipher_screen)
        self.key_label.setFont(font)
        
        self.key_input = QLineEdit(self.cipher_screen)
        self.key_input.setFont(font)

        # Şifreleme yöntemi seçimi
        self.method_label = QLabel('Şifreleme Yöntemi Seçin:', self.cipher_screen)
        self.method_label.setFont(font)
        
        self.method_combo = QComboBox(self.cipher_screen)
        self.method_combo.setFont(font)
        self.method_combo.addItem("Sezar (Caesar)")
        self.method_combo.addItem("RSA")
        self.method_combo.addItem("AES")
        
        self.encrypt_button = QPushButton('Şifrele', self.cipher_screen)
        self.encrypt_button.setFont(button_font)
        self.encrypt_button.clicked.connect(self.encrypt_message)

        self.decrypt_button = QPushButton('Çöz', self.cipher_screen)
        self.decrypt_button.setFont(button_font)
        self.decrypt_button.clicked.connect(self.decrypt_message)

        self.result_label = QLabel('Sonuç:', self.cipher_screen)
        self.result_label.setFont(font)
        
        self.result_output = QLineEdit(self.cipher_screen)
        self.result_output.setFont(font)

        # Excel dosyasını açma butonu
        self.open_excel_button = QPushButton('Excel Dosyasını Aç', self.cipher_screen)
        self.open_excel_button.setFont(button_font)
        self.open_excel_button.setObjectName("excelButton")  # Stil için id belirledik
        self.open_excel_button.clicked.connect(open_excel_file)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)

        cipher_layout.addWidget(self.version_label)
        cipher_layout.addWidget(self.message_label)
        cipher_layout.addWidget(self.message_input)
        cipher_layout.addWidget(self.key_label)
        cipher_layout.addWidget(self.key_input)
        cipher_layout.addWidget(self.method_label)
        cipher_layout.addWidget(self.method_combo)
        cipher_layout.addLayout(button_layout)
        cipher_layout.addWidget(self.result_label)
        cipher_layout.addWidget(self.result_output)
        cipher_layout.addWidget(self.open_excel_button)

        self.cipher_screen.hide()  # Şifreleme ekranı başlangıçta gizli

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.welcome_screen)
        main_layout.addWidget(self.cipher_screen)
        self.setLayout(main_layout)

    def show_cipher_screen(self):
        self.welcome_screen.hide()
        self.cipher_screen.show()

    def encrypt_message(self):
        message = self.message_input.text()
        method = self.method_combo.currentText()
        
        if method == "Sezar (Caesar)":
            shift_amount = random.randint(1, len(characters) - 1)
            encrypted_message = encrypt(message, shift_amount)
            key = f"{shift_amount}"
        
        elif method == "RSA":
            private_key, public_key = generate_rsa_keys()
            encrypted_message = rsa_encrypt(public_key, message)
            self.private_key = private_key  # Özel anahtarı saklayın
            key = private_key
        
        elif method == "AES":
            key = generate_aes_key()
            encrypted_message = aes_encrypt(key, message)
            key = key.hex()  # Anahtarı hex formatında göster
        
        self.result_output.setText(encrypted_message.hex() if isinstance(encrypted_message, bytes) else encrypted_message)
        self.key_input.setText(key)
        
        log_to_excel(self.result_output.text(), key)

    def decrypt_message(self):
        message = bytes.fromhex(self.result_output.text())
        method = self.method_combo.currentText()
        
        if method == "Sezar (Caesar)":
            try:
                shift_amount = int(self.key_input.text())
                decrypted_message = decrypt(message.decode(), shift_amount)
            except ValueError:
                self.result_output.setText("Geçersiz Anahtar")
                return
        
        elif method == "RSA":
            decrypted_message = rsa_decrypt(self.private_key, message)
        
        elif method == "AES":
            key = bytes.fromhex(self.key_input.text())
            decrypted_message = aes_decrypt(key, message)
        
        self.result_output.setText(decrypted_message)

