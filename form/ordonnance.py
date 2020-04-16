# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ordonnance.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class Ui_ordonnace(object):
    def insert_ordonnance(self):
        from Database import connexion
        from saisie_Id import identify
        from ficheMed import Ui_FicheMed,d,nm #d represente la date ne pas effacer
        nom_med = nm
        conx,cur = connexion()
        try:
            cur.execute("""SELECT id_med FROM medecin WHERE nom="{}" """.format(nom_med)) #On recupère l'id du medecin
        except Exception as e:
            print("error select id_med :",e)

        res = cur.fetchall()
        print("len = ",len(res))
        id_med = res[0][0]

        medicaments = self.text_ordonnace.toPlainText()
        element =(medicaments,d[0],id_med,identify)
        try:
            cur.execute("""INSERT INTO ordonnance(medicaments,date,id_med,id_patient) VALUES(?,?,?,?)""",element)
            print("SQL INSERTION TABLE ordonance --> ok")
            conx.commit()
            msg = QMessageBox()
            msg.setWindowTitle("Succes")
            msg.setText("Enregistrement effectué avec succes")
            msg.exec_()
        except Exception as e:
            print('Error in ordonance : ',e)
            print('SQL --> fail')
            msg = QMessageBox()
            msg.setWindowTitle("Echec")
            msg.setText("Echec de connexion")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

        conx.close()

    def setupUi(self, ordonnace):
        from ficheMed import nom,prenom,Ui_FicheMed,nm
        nom_med = nm
        ordonnace.setObjectName("ordonnace")
        ordonnace.resize(614, 640)
        ordonnace.setMinimumSize(QtCore.QSize(614, 640))
        ordonnace.setMaximumSize(QtCore.QSize(614, 640))
        self.centralwidget = QtWidgets.QWidget(ordonnace)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 130, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.date_ordonnance = QtWidgets.QDateEdit(self.centralwidget)
        self.date_ordonnance.setGeometry(QtCore.QRect(20, 80, 81, 21))
        self.date_ordonnance.setWrapping(False)
        self.date_ordonnance.setFrame(False)
        self.date_ordonnance.setAccelerated(False)
        self.date_ordonnance.setKeyboardTracking(True)
        self.date_ordonnance.setProperty("showGroupSeparator", False)
        self.date_ordonnance.setCalendarPopup(True)
        self.date_ordonnance.setObjectName("date_ordonnance")
        self.text_ordonnace = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_ordonnace.setGeometry(QtCore.QRect(10, 170, 591, 381))
        self.text_ordonnace.setPlainText("")
        self.text_ordonnace.setObjectName("text_ordonnace")
        self.boutton_enregistrer_ordonnance = QtWidgets.QPushButton(self.centralwidget)
        self.boutton_enregistrer_ordonnance.setGeometry(QtCore.QRect(320, 570, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.boutton_enregistrer_ordonnance.setFont(font)
        self.boutton_enregistrer_ordonnance.setObjectName("boutton_enregistrer_ordonnance")
        self.boutton_annuler_ordonnance = QtWidgets.QPushButton(self.centralwidget)
        self.boutton_annuler_ordonnance.setGeometry(QtCore.QRect(140, 570, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.boutton_annuler_ordonnance.setFont(font)
        self.boutton_annuler_ordonnance.setObjectName("boutton_annuler_ordonnance")
        self.label_patient_ordonnance = QtWidgets.QLabel(self.centralwidget)
        self.label_patient_ordonnance.setGeometry(QtCore.QRect(120, 120, 221, 31))
        self.label_patient_ordonnance.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_patient_ordonnance.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_patient_ordonnance.setText("{} {}".format(nom,prenom))
        self.label_patient_ordonnance.setObjectName("label_patient_ordonnance")
        self.label_medecin_ordonnance = QtWidgets.QLabel(self.centralwidget)
        self.label_medecin_ordonnance.setGeometry(QtCore.QRect(430, 120, 171, 31))
        self.label_medecin_ordonnance.setToolTip("")
        self.label_medecin_ordonnance.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_medecin_ordonnance.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_medecin_ordonnance.setText("{}".format(nom_med))
        self.label_medecin_ordonnance.setObjectName("label_medecin_ordonnance")
        ordonnace.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ordonnace)
        self.statusbar.setObjectName("statusbar")
        ordonnace.setStatusBar(self.statusbar)

        self.retranslateUi(ordonnace)
        QtCore.QMetaObject.connectSlotsByName(ordonnace)
        self.boutton_enregistrer_ordonnance.clicked.connect(self.insert_ordonnance)

    def retranslateUi(self, ordonnace):
        _translate = QtCore.QCoreApplication.translate
        ordonnace.setWindowTitle(_translate("ordonnace", "Ordonnace"))
        self.label.setText(_translate("ordonnace", "ORDONNANCE"))
        self.label_3.setText(_translate("ordonnace", "Nom et Prenoms : "))
        self.label_4.setText(_translate("ordonnace", "Medecin:"))
        self.boutton_enregistrer_ordonnance.setText(_translate("ordonnace", "Enregistrer"))
        self.boutton_annuler_ordonnance.setText(_translate("ordonnace", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ordonnace = QtWidgets.QMainWindow()
    ui = Ui_ordonnace()
    ui.setupUi(ordonnace)
    ordonnace.show()
    sys.exit(app.exec_())
