# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accueil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from consul import Ui_Consultation
from saisie_Id import Ui_SaisieId

class Ui_Accueil(object):
    def overture_de_fenetre_consul(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_Consultation()
        self.ui.setupUi(self.Window)
        Accueil.hide()
        self.Window.show()

    def overture_de_fenetre_saisie_id(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_SaisieId()
        self.ui.setupUi(self.Window)
        Accueil.hide()
        self.Window.show()


    def setupUi(self, Accueil):
        Accueil.setObjectName("Accueil")
        Accueil.resize(691, 489)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        Accueil.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Accueil)
        self.centralwidget.setObjectName("centralwidget")
        self.acceul = QtWidgets.QLabel(self.centralwidget)
        self.acceul.setGeometry(QtCore.QRect(220, 80, 241, 41))
        self.acceul.setObjectName("acceul")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 220, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 220, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 160, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        Accueil.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Accueil)
        self.statusbar.setObjectName("statusbar")
        Accueil.setStatusBar(self.statusbar)
        self.actionenregistre = QtWidgets.QAction(Accueil)
        self.actionenregistre.setObjectName("actionenregistre")
        self.actionquitter = QtWidgets.QAction(Accueil)
        self.actionquitter.setObjectName("actionquitter")
        self.actionouvrire = QtWidgets.QAction(Accueil)
        self.actionouvrire.setObjectName("actionouvrire")

        self.retranslateUi(Accueil)
        QtCore.QMetaObject.connectSlotsByName(Accueil)

        self.pushButton.clicked.connect(self.overture_de_fenetre_consul)
        self.pushButton_2.clicked.connect(self.overture_de_fenetre_saisie_id)

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "MainWindow"))
        self.acceul.setText(_translate("Accueil", "ACCEUIL"))
        self.pushButton.setText(_translate("Accueil", "consultation"))
        self.pushButton_2.setText(_translate("Accueil", "rendez-vous"))
        self.label_2.setText(_translate("Accueil", "bonjour Mr ou Mme vous êtes venus pour ?"))
        self.actionenregistre.setText(_translate("Accueil", "enregistre"))
        self.actionenregistre.setShortcut(_translate("Accueil", "Ctrl+S"))
        self.actionquitter.setText(_translate("Accueil", "quitter"))
        self.actionouvrire.setText(_translate("Accueil", "ouvrire"))
        self.actionouvrire.setShortcut(_translate("Accueil", "Ctrl+O"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accueil = QtWidgets.QMainWindow()
    ui = Ui_Accueil()
    ui.setupUi(Accueil)
    Accueil.show()
    sys.exit(app.exec_())

