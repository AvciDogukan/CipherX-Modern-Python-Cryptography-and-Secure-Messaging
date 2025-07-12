# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:49:44 2024

@author: Dogukan Avcı


"""

# main.py
import sys
from PyQt5.QtWidgets import QApplication
from main_window import CipherApp
from styles import get_stylesheet

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CipherApp()
    ex.setStyleSheet(get_stylesheet())
    ex.show()
    sys.exit(app.exec_())
