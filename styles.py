# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:49:01 2024

@author: Dogukan Avcı

Styles
"""

# styles.py
def get_stylesheet():
    return """
        * {
            font-family: 'Montserrat', sans-serif;
            font-size: 16px;
        }
        QWidget {
            background-color: #393937;
            color: #fff;
        }
        QPushButton {
            background-color: transparent;
            color: #03e9f4;
            padding: 20px 30px;
            text-transform: uppercase;
            letter-spacing: 4px;
            border: none;
            position: relative;
            overflow: hidden;
            transition: 0.5s;
        }
        QLabel {
            background-color: transparent;
            color: #03e9f4;
            padding: 20px 30px;
            text-transform: uppercase;
            letter-spacing: 4px;
            border: none;
            position: relative;
            overflow: hidden;
            transition: 0.5s;
        }
        QPushButton:hover {
            color: #fff;
        }
        QPushButton::before, QPushButton::after {
            content: '';
            position: absolute;
            background: #03e9f4;
            transition: 0.5s;
        }
        QPushButton::before {
            height: 2px;
            width: 100%;
            left: -100%;
            top: 0;
        }
        QPushButton::after {
            width: 2px;
            height: 100%;
            right: 0;
            top: -100%;
        }
        QPushButton:hover::before {
            left: 0;
        }
        QPushButton:hover::after {
            top: 0;
        }
        QLineEdit {
            background-color: #404040;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
        QPushButton#excelButton {
            background-color: #FFA500;
        }
        QPushButton#excelButton:hover {
            background-color: #FF8C00;
        }
    """
