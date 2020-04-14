# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\saisie_Id.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ficheMed import *
import sqlite3
# from accueil import Ui_Accueil  #Brindou



class Ui_SaisieId(object):
    # def retour_accueil(self):                     #Brindou
    #     self.Window = QtWidgets.QMainWindow()     #Brindou
    #     self.ui = Ui_Accueil()                    #Brindou
    #     self.ui.setupUi(self.Window)              #Brindou
    #     SaisieId.hide()                           #Brindou
    #     self.Window.show()                        #Brindou

    def verify_handler(self):
        id_patient = self.id_Patient.text()
        conx = sqlite3.connect('../config/santeplus.db')
        cur = conx.cursor()
        try:
            cur.execute("""SELECT * FROM patient WHERE id_patient ="{}" """.format(id_patient))
            print("ok")
        except Exception as e:
            print("error: ",e)
            print("Vous n'êtes pas inscrit!!")
        res= cur.fetchall()
        if len(res)!=0:
            self.open_ficheMed()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Echec")
            msg.setText("Vous n'êtes pas inscrit")

    def setupUi(self, SaisieId):
        SaisieId.setObjectName("SaisieId")
        SaisieId.setWindowModality(QtCore.Qt.NonModal)
        SaisieId.resize(437, 208)
        SaisieId.setMaximumSize(QtCore.QSize(437, 208))
        SaisieId.setMinimumSize(QtCore.QSize(437, 208))
        SaisieId.setMouseTracking(True)
        SaisieId.setFocusPolicy(QtCore.Qt.TabFocus)
        SaisieId.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        SaisieId.setAutoFillBackground(False)
        # SaisieId.setSizeGripEnabled(True)
        # SaisieId.setModal(False)
        self.label = QtWidgets.QLabel(SaisieId)
        self.label.setGeometry(QtCore.QRect(100, 40, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.id_Patient = QtWidgets.QLineEdit(SaisieId)
        self.id_Patient.setGeometry(QtCore.QRect(70, 110, 291, 31))
        self.id_Patient.setObjectName("id_Patient")
        self.boutton_Valider_Id = QtWidgets.QPushButton(SaisieId)
        self.boutton_Valider_Id.setGeometry(QtCore.QRect(250, 162, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.boutton_Valider_Id.setFont(font)
        self.boutton_Valider_Id.setObjectName("boutton_Valider_Id")
        self.button_Annuler_Id = QtWidgets.QPushButton(SaisieId)
        self.button_Annuler_Id.setGeometry(QtCore.QRect(100, 162, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_Annuler_Id.setFont(font)
        self.button_Annuler_Id.setObjectName("button_Annuler_Id")

        self.retranslateUi(SaisieId)
        QtCore.QMetaObject.connectSlotsByName(SaisieId)
        self.boutton_Valider_Id.clicked.connect(self.verify_handler)

        # self.button_Annuler_Id.clicked.connect(self.retour_accueil)

    def open_ficheMed(self):
        self.ficheMed = QtWidgets.QMainWindow()
        self.ui = Ui_FicheMed()
        self.ui.setupUi(self.ficheMed)
        # SaisieId.hide()
        self.ficheMed.show()

    def retranslateUi(self, SaisieId):
        _translate = QtCore.QCoreApplication.translate
        SaisieId.setWindowTitle(_translate("SaisieId", "Saisie du Numero Unique"))
        self.label.setText(_translate("SaisieId", "Numero Unique"))
        self.boutton_Valider_Id.setText(_translate("SaisieId", "Valider"))
        self.button_Annuler_Id.setText(_translate("SaisieId", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SaisieId = QtWidgets.QMainWindow()
    ui = Ui_SaisieId()
    ui.setupUi(SaisieId)
    SaisieId.show()
    sys.exit(app.exec_())
