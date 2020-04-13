# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accueil.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.acceul = QtWidgets.QLabel(self.centralwidget)
        self.acceul.setGeometry(QtCore.QRect(270, 80, 241, 41))
        self.acceul.setObjectName("acceul")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 220, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 210, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 160, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menufichier = QtWidgets.QMenu(self.menubar)
        self.menufichier.setObjectName("menufichier")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionenregistre = QtWidgets.QAction(MainWindow)
        self.actionenregistre.setObjectName("actionenregistre")
        self.actionquitter = QtWidgets.QAction(MainWindow)
        self.actionquitter.setObjectName("actionquitter")
        self.actionouvrire = QtWidgets.QAction(MainWindow)
        self.actionouvrire.setObjectName("actionouvrire")
        self.menufichier.addAction(self.actionenregistre)
        self.menufichier.addAction(self.actionouvrire)
        self.menufichier.addAction(self.actionquitter)
        self.menubar.addAction(self.menufichier.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.acceul.setText(_translate("MainWindow", "ACCEUIL"))
        self.pushButton.setText(_translate("MainWindow", "consultation"))
        self.pushButton_2.setText(_translate("MainWindow", "rendez-vous"))
        self.label_2.setText(_translate("MainWindow", "bonjour Mr ou Mme vous êtes venus pour ?"))
        self.menufichier.setTitle(_translate("MainWindow", "fichier"))
        self.actionenregistre.setText(_translate("MainWindow", "enregistre"))
        self.actionenregistre.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionquitter.setText(_translate("MainWindow", "quitter"))
        self.actionouvrire.setText(_translate("MainWindow", "ouvrire"))
        self.actionouvrire.setShortcut(_translate("MainWindow", "Ctrl+O"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

