# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from time import time, sleep
import pysrc
import sys


#Fonctions

# Chargement de la page
def open_ui_load():
    global LOAD, ui
    LOAD = QtWidgets.QFrame()
    ui = Ui_Load()
    ui.setupUi(LOAD)
    LOAD.show()
    for i in range(1, 999):
        ui.progressBar.setValue(i)
        t = time()
        while time() < t + 0.004:
            app.processEvents()
    ui.open_login()

#Ouverture de de login
def open_ui_login():
    global LOGIN, ui
    LOGIN = QtWidgets.QFrame()
    ui = Ui_login()
    ui.setupUi(LOGIN)
    LOGIN.show()


def open_ui_():
    global LOGIN, ui
    LOGIN = QtWidgets.QFrame()
    ui = Ui_Login()
    ui.setupUi(LOGIN)
    LOGIN.show()