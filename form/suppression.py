# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suppression.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(659, 570)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 601, 361))
        self.groupBox.setStyleSheet("Border-radius: 10px;\n"
"background-color: rgb(218, 218, 218);")
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(130, 80, 331, 201))
        self.frame.setStyleSheet("background-color: rgb(127, 127, 127);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.label_3.setObjectName("label_3")
        self.no_compte_sup = QtWidgets.QLineEdit(self.frame)
        self.no_compte_sup.setGeometry(QtCore.QRect(100, 80, 211, 21))
        self.no_compte_sup.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 5px;")
        self.no_compte_sup.setObjectName("no_compte_sup")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 281, 41))
        self.label.setObjectName("label")
        self.bouton_sup = QtWidgets.QPushButton(self.frame)
        self.bouton_sup.setGeometry(QtCore.QRect(30, 140, 121, 23))
        self.bouton_sup.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius:10px;")
        self.bouton_sup.setObjectName("bouton_sup")
        self.annuler_sup = QtWidgets.QPushButton(self.frame)
        self.annuler_sup.setGeometry(QtCore.QRect(180, 140, 121, 23))
        self.annuler_sup.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius:10px;")
        self.annuler_sup.setObjectName("annuler_sup")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("mainWindow", "Suppression"))
        self.label_3.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">N° de compte:</span></p></body></html>"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Suppression du patient...</span></p></body></html>"))
        self.bouton_sup.setToolTip(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">CONNECTION</span></p></body></html>"))
        self.bouton_sup.setWhatsThis(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">CONNECTION</span></p><p align=\"center\"><br/></p></body></html>"))
        self.bouton_sup.setText(_translate("mainWindow", "SUPPRIMER"))
        self.annuler_sup.setToolTip(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">CONNECTION</span></p></body></html>"))
        self.annuler_sup.setWhatsThis(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">CONNECTION</span></p><p align=\"center\"><br/></p></body></html>"))
        self.annuler_sup.setText(_translate("mainWindow", "ANNULER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

