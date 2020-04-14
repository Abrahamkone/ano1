# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consul.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from inscrit import Ui_Inscrit

class Ui_Consultation(object):
    
    def overture_de_fenetre_inscription(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_Inscrit()
        self.ui.setupUi(self.Window)
        self.Window.show()


    def setupUi(self, Consultation):
        Consultation.setObjectName("Consultation")
        Consultation.resize(651, 337)
        self.centralwidget = QtWidgets.QWidget(Consultation)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 190, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 190, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        Consultation.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Consultation)
        self.statusbar.setObjectName("statusbar")
        Consultation.setStatusBar(self.statusbar)

        self.retranslateUi(Consultation)
        QtCore.QMetaObject.connectSlotsByName(Consultation)

        # pushButton les gars nom des variables la c'est pas tro sa hin
        self.pushButton.clicked.connect(self.overture_de_fenetre_inscription)


    def retranslateUi(self, Consultation):
        _translate = QtCore.QCoreApplication.translate
        Consultation.setWindowTitle(_translate("Consultation", "MainWindow"))
        self.label.setText(_translate("Consultation", "CONSULTATION"))
        self.pushButton.setText(_translate("Consultation", "NOUVEAU"))
        self.pushButton_2.setText(_translate("Consultation", "ANCIEN"))
        self.label_2.setText(_translate("Consultation", "êtes vous nouveau ou ancien?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Consultation = QtWidgets.QMainWindow()
    ui = Ui_Consultation()
    ui.setupUi(Consultation)
    Consultation.show()
    sys.exit(app.exec_())

