# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:47:28 2024

@author: Dogukan Avcı
Cipher Functions
"""

# cipher_functions.py
# cipher_functions.py
import random
import string
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# Mevcut Karakter Seti
characters = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ0123456789"

# RSA Şifreleme için anahtar üretme
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# RSA ile şifreleme
def rsa_encrypt(public_key, message):
    encrypted = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# RSA ile çözme
def rsa_decrypt(private_key, encrypted_message):
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode('utf-8')

# AES Şifreleme için anahtar oluşturma
def generate_aes_key():
    key = os.urandom(32)  # 256 bit anahtar
    return key

# AES ile şifreleme
def aes_encrypt(key, message):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode('utf-8')) + encryptor.finalize()
    return iv + encrypted_message  # IV ve şifreli mesajı birleştiriyoruz

# AES ile çözme
def aes_decrypt(key, encrypted_message):
    iv = encrypted_message[:16]
    actual_encrypted_message = encrypted_message[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(actual_encrypted_message) + decryptor.finalize()
    return decrypted_message.decode('utf-8')

# Mevcut Sezar Şifreleme Fonksiyonları
def encrypt(text, shift_amount):
    encrypted_text = ""
    for char in text:
        if char.upper() in characters:
            index = characters.index(char.upper())
            new_index = (index + shift_amount) % len(characters)
            if char.isupper():
                encrypted_text += characters[new_index]
            else:
                encrypted_text += characters[new_index].lower()
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift_amount):
    decrypted_text = ""
    for char in text:
        if char.upper() in characters:
            index = characters.index(char.upper())
            new_index = (index - shift_amount) % len(characters)
            if char.isupper():
                decrypted_text += characters[new_index]
            else:
                decrypted_text += characters[new_index].lower()
        else:
            decrypted_text += char
    return decrypted_text

def generate_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
