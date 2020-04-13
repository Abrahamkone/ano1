# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 601, 511))
        self.groupBox.setStyleSheet("Border-radius: 10px;\n"
"background-color: rgb(218, 218, 218);")
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(130, 110, 331, 291))
        self.frame.setStyleSheet("background-color: rgb(127, 127, 127);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.username_log = QtWidgets.QLineEdit(self.frame)
        self.username_log.setGeometry(QtCore.QRect(100, 80, 211, 21))
        self.username_log.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 5px;")
        self.username_log.setObjectName("username_log")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(100, 140, 211, 21))
        self.password.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 5px;")
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 111, 51))
        self.label.setObjectName("label")
        self.connexion = QtWidgets.QPushButton(self.frame)
        self.connexion.setGeometry(QtCore.QRect(100, 210, 121, 23))
        self.connexion.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);\n"
"border-radius:10px;")
        self.connexion.setObjectName("connexion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hospital"))
        self.groupBox.setTitle(_translate("MainWindow", "Ouverture de session"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">USERNAME :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">PASSWORD :</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Login...</span></p></body></html>"))
        self.connexion.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">CONNECTION</span></p></body></html>"))
        self.connexion.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">CONNECTION</span></p><p align=\"center\"><br/></p></body></html>"))
        self.connexion.setText(_translate("MainWindow", "CONNECTION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

