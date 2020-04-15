# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saisie_Id_rdv.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class Ui_SaisieId_rdv(object):

    def verify_handler(self):
        global identify
        id_patient_rdv = self.id_Patient_rdv.text()
        conx = sqlite3.connect('C:/Users/DIARRASSOUBA Siaka/Documents/GitHub/ano1/config/santeplus.db')
        cur = conx.cursor()
        try:
            cur.execute("""SELECT * FROM patient WHERE id_patient ="{}" """.format(id_patient_rdv))
            print("SQL --> ok")
        except Exception as e:
            print("error: ",e)
            print("SQL --> fail")
        res= cur.fetchall()
        if len(res)!=0:
            identify= res[0][0]
            print("id =",identify)
            self.open_ficheMed()
        else:
            print("id =",identify)
            msg = QMessageBox()
            msg.setWindowTitle("Echec")
            msg.setText("Vous n'êtes pas inscrit")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()



    def setupUi(self, SaisieId_rdv):
        SaisieId_rdv.setObjectName("SaisieId_rdv")
        SaisieId_rdv.setWindowModality(QtCore.Qt.NonModal)
        SaisieId_rdv.resize(437, 208)
        SaisieId_rdv.setMinimumSize(QtCore.QSize(437, 0))
        SaisieId_rdv.setMaximumSize(QtCore.QSize(437, 208))
        SaisieId_rdv.setMouseTracking(True)
        SaisieId_rdv.setFocusPolicy(QtCore.Qt.TabFocus)
        SaisieId_rdv.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        SaisieId_rdv.setAutoFillBackground(False)
        SaisieId_rdv.setSizeGripEnabled(True)
        SaisieId_rdv.setModal(False)
        self.label = QtWidgets.QLabel(SaisieId_rdv)
        self.label.setGeometry(QtCore.QRect(100, 40, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.id_Patient_rdv = QtWidgets.QTextBrowser(SaisieId_rdv)
        self.id_Patient_rdv.setGeometry(QtCore.QRect(70, 110, 291, 31))
        self.id_Patient_rdv.setMouseTracking(True)
        self.id_Patient_rdv.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.id_Patient_rdv.setObjectName("id_Patient_rdv")
        self.boutton_Valider_Id_rdv = QtWidgets.QPushButton(SaisieId_rdv)
        self.boutton_Valider_Id_rdv.setGeometry(QtCore.QRect(250, 162, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.boutton_Valider_Id_rdv.setFont(font)
        self.boutton_Valider_Id_rdv.setObjectName("boutton_Valider_Id_rdv")
        self.button_Annuler_Id_rdv = QtWidgets.QPushButton(SaisieId_rdv)
        self.button_Annuler_Id_rdv.setGeometry(QtCore.QRect(100, 162, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_Annuler_Id_rdv.setFont(font)
        self.button_Annuler_Id_rdv.setObjectName("button_Annuler_Id_rdv")

        self.retranslateUi(SaisieId_rdv)
        QtCore.QMetaObject.connectSlotsByName(SaisieId_rdv)

    def retranslateUi(self, SaisieId_rdv):
        _translate = QtCore.QCoreApplication.translate
        SaisieId_rdv.setWindowTitle(_translate("SaisieId_rdv", "Saisie du Numero Unique"))
        self.label.setText(_translate("SaisieId_rdv", "Numero Unique"))
        self.boutton_Valider_Id_rdv.setText(_translate("SaisieId_rdv", "Valider"))
        self.button_Annuler_Id_rdv.setText(_translate("SaisieId_rdv", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SaisieId_rdv = QtWidgets.QDialog()
    ui = Ui_SaisieId_rdv()
    ui.setupUi(SaisieId_rdv)
    SaisieId_rdv.show()
    sys.exit(app.exec_())
