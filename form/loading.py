# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import img_rc
import sys
import time
from login import *

class Ui_Loging(object):

    def suivant(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        self.window.show()
        Loging.hide()

    def setupUi(self, Loging):
        Loging.setObjectName("Loging")
        Loging.resize(628, 468)
        self.centralwidget = QtWidgets.QWidget(Loging)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 601, 401))
        self.groupBox.setStyleSheet("Border-radius: 10px;\n""background-color: rgb(218, 218, 218);")
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(130, 80, 331, 221))
        self.frame.setStyleSheet("background-color: rgb(127, 127, 127);\n""border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 51))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(47, 120, 241, 31))
        self.progressBar.setStyleSheet("border-radius: 5px;\n""background-color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        Loging.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Loging)
        self.statusbar.setObjectName("statusbar")
        Loging.setStatusBar(self.statusbar)

        self.retranslateUi(Loging)
        QtCore.QMetaObject.connectSlotsByName(Loging)

    def retranslateUi(self, Loging):
        _translate = QtCore.QCoreApplication.translate
        Loging.setWindowTitle(_translate("Loging", "Hospital"))
        self.groupBox.setTitle(_translate("Loging", "Ouverture de session"))
        self.label.setText(_translate("Loging", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Loading...</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Loging = QtWidgets.QMainWindow()
    ui = Ui_Loging()
    ui.setupUi(Loging)
    Loging.show()
    for i in range(1, 999):
        ui.progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.009:
           app.processEvents()
    ui.suivant()
    sys.exit(app.exec_())
