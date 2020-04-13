# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inscrit.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 50, 651, 501))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QLineEdit{\n"
"    color: rgb(239, 239, 239);\n"
"    color: rgb(238, 238, 238);\n"
"background-color: rgb(188, 188, 188);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.photo = QtWidgets.QLabel(self.groupBox)
        self.photo.setGeometry(QtCore.QRect(540, 10, 101, 101))
        self.photo.setStyleSheet("\n"
"background-color: rgb(203, 203, 203);")
        self.photo.setObjectName("photo")
        self.prenomClient = QtWidgets.QLineEdit(self.groupBox)
        self.prenomClient.setGeometry(QtCore.QRect(410, 180, 141, 21))
        self.prenomClient.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.prenomClient.setObjectName("prenomClient")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(340, 230, 31, 16))
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(330, 180, 47, 13))
        self.label_4.setObjectName("label_4")
        self.nomClient = QtWidgets.QLineEdit(self.groupBox)
        self.nomClient.setGeometry(QtCore.QRect(120, 180, 131, 21))
        self.nomClient.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.nomClient.setText("")
        self.nomClient.setObjectName("nomClient")
        self.tool = QtWidgets.QToolButton(self.groupBox)
        self.tool.setGeometry(QtCore.QRect(620, 120, 25, 19))
        self.tool.setObjectName("tool")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(560, 120, 61, 16))
        self.label_13.setObjectName("label_13")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(310, 270, 91, 16))
        self.label_5.setObjectName("label_5")
        self.date = QtWidgets.QDateEdit(self.groupBox)
        self.date.setGeometry(QtCore.QRect(440, 270, 81, 22))
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.prof = QtWidgets.QLineEdit(self.groupBox)
        self.prof.setGeometry(QtCore.QRect(120, 220, 131, 21))
        self.prof.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.prof.setObjectName("prof")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 61, 16))
        self.label_10.setObjectName("label_10")
        self.nation = QtWidgets.QLineEdit(self.groupBox)
        self.nation.setGeometry(QtCore.QRect(120, 280, 131, 21))
        self.nation.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nation.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.nation.setObjectName("nation")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 220, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 330, 47, 13))
        self.label_8.setObjectName("label_8")
        self.cni_Client = QtWidgets.QLineEdit(self.groupBox)
        self.cni_Client.setGeometry(QtCore.QRect(420, 310, 131, 21))
        self.cni_Client.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.cni_Client.setObjectName("cni_Client")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(310, 310, 71, 16))
        self.label_11.setObjectName("label_11")
        self.cont = QtWidgets.QLineEdit(self.groupBox)
        self.cont.setGeometry(QtCore.QRect(120, 320, 141, 21))
        self.cont.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.cont.setObjectName("cont")
        self.mail = QtWidgets.QLineEdit(self.groupBox)
        self.mail.setGeometry(QtCore.QRect(120, 360, 131, 21))
        self.mail.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.mail.setObjectName("mail")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(30, 370, 41, 16))
        self.label_12.setObjectName("label_12")
        self.ann = QtWidgets.QPushButton(self.groupBox)
        self.ann.setGeometry(QtCore.QRect(190, 450, 81, 23))
        self.ann.setObjectName("ann")
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(310, 450, 20, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.save = QtWidgets.QPushButton(self.groupBox)
        self.save.setGeometry(QtCore.QRect(370, 450, 91, 23))
        self.save.setObjectName("save")
        self.sexe = QtWidgets.QComboBox(self.groupBox)
        self.sexe.setGeometry(QtCore.QRect(420, 230, 131, 22))
        self.sexe.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.sexe.setObjectName("sexe")
        self.sexe.addItem("")
        self.sexe.setItemText(0, "")
        self.sexe.addItem("")
        self.sexe.addItem("")
        self.sexe_3 = QtWidgets.QComboBox(self.groupBox)
        self.sexe_3.setGeometry(QtCore.QRect(430, 370, 131, 22))
        self.sexe_3.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.sexe_3.setObjectName("sexe_3")
        self.sexe_3.addItem("")
        self.sexe_3.setItemText(0, "")
        self.sexe_3.addItem("")
        self.sexe_3.addItem("")
        self.sexe_3.addItem("")
        self.sexe_3.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(340, 370, 61, 16))
        self.label.setObjectName("label")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(60, 10, 121, 31))
        self.label_15.setStyleSheet("\n"
"color: rgb(170, 0, 0);")
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "OUVERTURE DE COMPTE"))
        self.photo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">photo</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Nom:"))
        self.label_7.setText(_translate("MainWindow", "Sexe:"))
        self.label_4.setText(_translate("MainWindow", "Prénom:"))
        self.tool.setText(_translate("MainWindow", "..."))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Parcourir:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Date de naissance:"))
        self.label_10.setText(_translate("MainWindow", "Nationalité:"))
        self.nation.setPlaceholderText(_translate("MainWindow", "ivoirienne"))
        self.label_9.setText(_translate("MainWindow", "Profession:"))
        self.label_8.setText(_translate("MainWindow", "Contact:"))
        self.cni_Client.setPlaceholderText(_translate("MainWindow", "CI"))
        self.label_11.setText(_translate("MainWindow", "N° de la CNI:"))
        self.cont.setPlaceholderText(_translate("MainWindow", "+225"))
        self.label_12.setText(_translate("MainWindow", "E-mail:"))
        self.ann.setText(_translate("MainWindow", "ANNULER"))
        self.save.setText(_translate("MainWindow", "ENREGISTRER"))
        self.sexe.setItemText(1, _translate("MainWindow", "HOMME"))
        self.sexe.setItemText(2, _translate("MainWindow", "FEMME"))
        self.sexe_3.setItemText(1, _translate("MainWindow", "axa"))
        self.sexe_3.setItemText(2, _translate("MainWindow", "assurace"))
        self.sexe_3.setItemText(3, _translate("MainWindow", "mugefci"))
        self.sexe_3.setItemText(4, _translate("MainWindow", "dangereux "))
        self.label.setText(_translate("MainWindow", "assurance:"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">santé +</span></p><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

