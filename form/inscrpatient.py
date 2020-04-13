# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inscrpatient.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
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
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sexe = QtWidgets.QComboBox(self.groupBox)
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
        self.horizontalLayout_2.addWidget(self.sexe)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.date = QtWidgets.QDateEdit(self.groupBox)
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.horizontalLayout_3.addWidget(self.date)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem3)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_27.addWidget(self.line_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_27, 8, 1, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tool = QtWidgets.QToolButton(self.groupBox)
        self.tool.setObjectName("tool")
        self.horizontalLayout.addWidget(self.tool)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 5, 1, 1)
        self.photo = QtWidgets.QLabel(self.groupBox)
        self.photo.setStyleSheet("\n"
"background-color: rgb(203, 203, 203);")
        self.photo.setObjectName("photo")
        self.gridLayout.addWidget(self.photo, 0, 4, 1, 2)
        self.cont_5 = QtWidgets.QLineEdit(self.groupBox)
        self.cont_5.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.cont_5.setObjectName("cont_5")
        self.gridLayout.addWidget(self.cont_5, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.prenomClient_5 = QtWidgets.QLineEdit(self.groupBox)
        self.prenomClient_5.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.prenomClient_5.setObjectName("prenomClient_5")
        self.gridLayout.addWidget(self.prenomClient_5, 2, 3, 1, 1)
        self.lieu = QtWidgets.QLineEdit(self.groupBox)
        self.lieu.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.lieu.setObjectName("lieu")
        self.gridLayout.addWidget(self.lieu, 6, 1, 1, 1)
        self.cni_Client = QtWidgets.QLineEdit(self.groupBox)
        self.cni_Client.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.cni_Client.setObjectName("cni_Client")
        self.gridLayout.addWidget(self.cni_Client, 7, 1, 1, 1)
        self.nation = QtWidgets.QLineEdit(self.groupBox)
        self.nation.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nation.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.nation.setObjectName("nation")
        self.gridLayout.addWidget(self.nation, 6, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 2, 1, 1)
        self.mail = QtWidgets.QLineEdit(self.groupBox)
        self.mail.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.mail.setObjectName("mail")
        self.gridLayout.addWidget(self.mail, 7, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.groupBox)
        self.label_51.setObjectName("label_51")
        self.gridLayout.addWidget(self.label_51, 3, 2, 1, 1)
        self.nomClient = QtWidgets.QLineEdit(self.groupBox)
        self.nomClient.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.nomClient.setText("")
        self.nomClient.setObjectName("nomClient")
        self.gridLayout.addWidget(self.nomClient, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.prof = QtWidgets.QLineEdit(self.groupBox)
        self.prof.setStyleSheet("border-color:black;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"")
        self.prof.setObjectName("prof")
        self.gridLayout.addWidget(self.prof, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)
        self.ann_2 = QtWidgets.QPushButton(self.groupBox)
        self.ann_2.setGeometry(QtCore.QRect(108, 428, 664, 23))
        self.ann_2.setObjectName("ann_2")
        self.save = QtWidgets.QPushButton(self.groupBox)
        self.save.setGeometry(QtCore.QRect(108, 457, 664, 23))
        self.save.setObjectName("save")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.groupBox)
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
        self.sexe.setItemText(1, _translate("MainWindow", "HOMME"))
        self.sexe.setItemText(2, _translate("MainWindow", "FEMME"))
        self.tool.setText(_translate("MainWindow", "..."))
        self.photo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">photo</p></body></html>"))
        self.cont_5.setPlaceholderText(_translate("MainWindow", "+225"))
        self.label_5.setText(_translate("MainWindow", "Date de naissance:"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">A</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Parcourir:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Nom:"))
        self.cni_Client.setPlaceholderText(_translate("MainWindow", "CI"))
        self.nation.setPlaceholderText(_translate("MainWindow", "ivoirienne"))
        self.label_12.setText(_translate("MainWindow", "E-mail:"))
        self.label_7.setText(_translate("MainWindow", "Sexe:"))
        self.label_51.setText(_translate("MainWindow", "Contact:"))
        self.label_9.setText(_translate("MainWindow", "Profession:"))
        self.label_11.setText(_translate("MainWindow", "N° de la CNI:"))
        self.label_10.setText(_translate("MainWindow", "Nationalité:"))
        self.label_14.setText(_translate("MainWindow", "Prénom:"))
        self.ann_2.setText(_translate("MainWindow", "ANNULER"))
        self.save.setText(_translate("MainWindow", "ENREGISTRER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
