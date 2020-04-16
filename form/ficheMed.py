# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ficheMed.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sqlite3
from datetime import datetime
from time import strftime

nom = "nomTest"
prenom = "prenomTest"
nm = "none"
d = str(datetime.now()).split(" ")

class Ui_FicheMed(object):

    def overture_de_fenetre_ordonnance(self):
        from ordonnance import Ui_ordonnace
        global nm
        nm = self.comboBox_medTrait.currentText()
        print("nom med ={} et date = {}".format(nm,d[0]))
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_ordonnace()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def select_value(self):
        from saisie_Id import identify
        from Database import connexion
        global nom, prenom
        print("value id = ",identify)
        conx,cur = connexion()
        try:
            cur.execute("""SELECT nom,prenom FROM patient WHERE id_patient ="{}" """.format(identify))
            print("SQL SELECT TABLE patient --> ok")
        except Exception as e:
            print("error: ",e)
            print("SQL --> fail")
        res= cur.fetchall()
        print(len(res))
        nom = res[0][0]
        prenom = res[0][1]
        conx.close()

    def insert_handler(self):
        from saisie_Id import identify
        from Database import connexion
        global nm
        date = d[0]
        heure = d[1]
        date_rdv = self.dateRDVDateEdit.date().toPyDate()
        service = self.serviceComboBox.currentText()
        id_patient = identify
        allergie = self.allergieComboBox.currentText()
        temperature = self.tempRatureLineEdit.text()
        observation = self.textEdit_Observation.toPlainText()
        symptome = self.lineEdit_Symptome.text()
        nom_med = self.comboBox_medTrait.currentText()
        nm = nom_med
        element = (date,heure,service,id_patient,allergie,temperature,observation,symptome,nom_med)
        element2 = (id_patient,date,heure,nom_med,service,date_rdv)
        conx,cur = connexion()
        try:
            cur.execute("""INSERT INTO consultation(date_consul,heure,service,id_patient,allergie,temperature,observation,symptome,nom_med) VALUES(?,?,?,?,?,?,?,?,?)""",element)
            conx.commit()
            print("SQL INSERTION TABLE consultation --> ok")
            if (date_rdv == "2000-01-01"):
                conx.close()
            else:
                try:
                    cur.execute("""INSERT INTO rdv(id_patient,date_consul,heure_consul,nom_med,service,date_rdv) VALUES(?,?,?,?,?,?)""",element2)
                    conx.commit()
                    print("SQL INSERTION TABLE rdv --> ok")
                    print(date_rdv)
                except Exception as e:
                    print('Error in rdv : ',e)
                    print('SQL --> fail')
            msg = QMessageBox()
            msg.setWindowTitle("Succes")
            msg.setText("Enregistrement effectué avec succes")
            msg.exec_()
        except Exception as e:
            print('Error in consultation : ',e)
            print('SQL --> fail')
            msg = QMessageBox()
            msg.setWindowTitle("Echec")
            msg.setText("Echec de connexion")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        conx.close()

    def setupUi(self, FicheMed):
        FicheMed.setObjectName("FicheMed")
        FicheMed.resize(916, 683)
        FicheMed.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(FicheMed)
        self.label.setGeometry(QtCore.QRect(0, 0, 141, 111))
        self.label.setStyleSheet("image: url(:/consul_img/img5.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(FicheMed)
        self.label_3.setGeometry(QtCore.QRect(190, 30, 531, 61))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setWhatsThis("")
        self.label_3.setStyleSheet("border-style:solid;\n"
"border-width:2px;\n"
"border-color:black;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FicheMed)
        self.label_4.setGeometry(QtCore.QRect(770, 0, 141, 111))
        self.label_4.setStyleSheet("image: url(:/consul_img/img5.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayoutWidget = QtWidgets.QWidget(FicheMed)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 130, 791, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setStyleSheet("")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 421, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 19, 401, 126))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(5, 0, 18, 0)
        self.formLayout.setSpacing(3)
        self.formLayout.setObjectName("formLayout")
        self.nomLabel = QtWidgets.QLabel(self.formLayoutWidget)

        #pour afficher les info du patient
        self.select_value()
        #---------------------------

        font = QtGui.QFont()
        font.setPointSize(10)
        self.nomLabel.setFont(font)
        self.nomLabel.setObjectName("nomLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nomLabel)
        self.nomLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nomLineEdit.setEnabled(False)
        self.nomLineEdit.setObjectName("nomLineEdit")

        self.nomLineEdit.setText(nom)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nomLineEdit)
        self.prNomsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prNomsLabel.setFont(font)
        self.prNomsLabel.setObjectName("prNomsLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.prNomsLabel)
        self.prNomsLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.prNomsLineEdit.setEnabled(False)
        self.prNomsLineEdit.setObjectName("prNomsLineEdit")

        self.prNomsLineEdit.setText(prenom)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prNomsLineEdit)
        self.ageLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ageLabel.setObjectName("ageLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ageLabel)
        self.ageLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ageLineEdit.setEnabled(False)
        self.ageLineEdit.setObjectName("ageLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ageLineEdit)
        self.poidsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.poidsLabel.setObjectName("poidsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.poidsLabel)
        self.poidsLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.poidsLineEdit.setEnabled(False)
        self.poidsLineEdit.setObjectName("poidsLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.poidsLineEdit)
        self.tailleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.tailleLabel.setObjectName("tailleLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.tailleLabel)
        self.tailleLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.tailleLineEdit.setEnabled(False)
        self.tailleLineEdit.setObjectName("tailleLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tailleLineEdit)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(450, 20, 321, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 301, 138))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 3, 0, 0)
        self.formLayout_2.setHorizontalSpacing(2)
        self.formLayout_2.setVerticalSpacing(8)
        self.formLayout_2.setObjectName("formLayout_2")
        self.allergieLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.allergieLabel.setFont(font)
        self.allergieLabel.setObjectName("allergieLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.allergieLabel)
        self.allergieComboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.allergieComboBox.setObjectName("allergieComboBox")
        self.allergieComboBox.addItem("")
        self.allergieComboBox.setItemText(0, "")
        self.allergieComboBox.addItem("")
        self.allergieComboBox.addItem("")
        self.allergieComboBox.addItem("")
        self.allergieComboBox.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.allergieComboBox)
        self.tempRatureLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.tempRatureLabel.setFont(font)
        self.tempRatureLabel.setObjectName("tempRatureLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.tempRatureLabel)
        self.tempRatureLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.tempRatureLineEdit.setObjectName("tempRatureLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tempRatureLineEdit)
        self.mDecinTraitantLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.mDecinTraitantLabel.setFont(font)
        self.mDecinTraitantLabel.setObjectName("mDecinTraitantLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.mDecinTraitantLabel)
        self.serviceLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.serviceLabel.setFont(font)
        self.serviceLabel.setObjectName("serviceLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.serviceLabel)
        self.serviceComboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.serviceComboBox.setObjectName("serviceComboBox")
        self.serviceComboBox.addItem("")
        self.serviceComboBox.setItemText(0, "")
        self.serviceComboBox.addItem("")
        self.serviceComboBox.addItem("")
        self.serviceComboBox.addItem("")
        self.serviceComboBox.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.serviceComboBox)
        self.comboBox_medTrait = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox_medTrait.setObjectName("comboBox_medTrait")
        self.comboBox_medTrait.addItem("")
        self.comboBox_medTrait.setItemText(0, "")
        self.comboBox_medTrait.addItem("")
        self.comboBox_medTrait.addItem("")
        self.comboBox_medTrait.addItem("")
        self.comboBox_medTrait.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_medTrait)
        self.dateRDVLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.dateRDVLabel.setObjectName("dateRDVLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.dateRDVLabel)
        self.dateRDVDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.dateRDVDateEdit.setObjectName("dateRDVDateEdit")
        self.dateRDVDateEdit.setCalendarPopup(True)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateRDVDateEdit)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 200, 421, 221))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit_Observation = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_Observation.setGeometry(QtCore.QRect(10, 20, 401, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_Observation.setFont(font)
        self.textEdit_Observation.setObjectName("textEdit_Observation")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(450, 200, 321, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_Symptome = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_Symptome.setGeometry(QtCore.QRect(80, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Symptome.setFont(font)
        self.lineEdit_Symptome.setStyleSheet("color: red;")
        self.lineEdit_Symptome.setObjectName("lineEdit_Symptome")
        self.commandLinkButtonOrdonance = QtWidgets.QCommandLinkButton(self.groupBox)
        self.commandLinkButtonOrdonance.setGeometry(QtCore.QRect(450, 340, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.commandLinkButtonOrdonance.setFont(font)
        self.commandLinkButtonOrdonance.setDefault(False)
        self.commandLinkButtonOrdonance.setObjectName("commandLinkButtonOrdonance")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 440, 361, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonTerminer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonTerminer.setFont(font)
        self.pushButtonTerminer.setStyleSheet("")
        self.pushButtonTerminer.setCheckable(False)
        self.pushButtonTerminer.setAutoDefault(True)
        self.pushButtonTerminer.setDefault(True)
        self.pushButtonTerminer.setFlat(False)
        self.pushButtonTerminer.setObjectName("pushButtonTerminer")
        self.verticalLayout.addWidget(self.pushButtonTerminer)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(FicheMed)
        self.pushButton.setGeometry(QtCore.QRect(770, 640, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(FicheMed)
        QtCore.QMetaObject.connectSlotsByName(FicheMed)
        self.pushButtonTerminer.clicked.connect(self.insert_handler)


        self.commandLinkButtonOrdonance.clicked.connect(self.overture_de_fenetre_ordonnance)


    def retranslateUi(self, FicheMed):
        _translate = QtCore.QCoreApplication.translate
        FicheMed.setWindowTitle(_translate("FicheMed", "Dialog"))
        self.label_3.setText(_translate("FicheMed", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline; color:#aaff00;\">FICHE MEDICALE</span></p></body></html>"))
        self.groupBox.setTitle(_translate("FicheMed", "Consultation"))
        self.groupBox_2.setTitle(_translate("FicheMed", "Information sur le patient"))
        self.nomLabel.setText(_translate("FicheMed", "<html><head/><body><p><span style=\" text-decoration: underline;\">Nom :</span></p></body></html>"))
        self.prNomsLabel.setText(_translate("FicheMed", "<html><head/><body><p><span style=\" text-decoration: underline;\">Prénoms :</span></p></body></html>"))
        self.ageLabel.setText(_translate("FicheMed", "<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline;\">Age :</span></p></body></html>"))
        self.poidsLabel.setText(_translate("FicheMed", "<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline;\">Poids :</span></p></body></html>"))
        self.tailleLabel.setText(_translate("FicheMed", "<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline;\">Taille</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("FicheMed", "Informations supplémentaires"))
        self.allergieLabel.setText(_translate("FicheMed", "Allergie :"))
        self.tempRatureLabel.setText(_translate("FicheMed", "Température:"))
        self.mDecinTraitantLabel.setText(_translate("FicheMed", "Médecin Traitant :"))
        self.serviceLabel.setText(_translate("FicheMed", "Service :"))
        self.dateRDVLabel.setText(_translate("FicheMed", "<html><head/><body><p><span style=\" font-size:10pt; text-decoration: underline;\">Date RDV:</span></p></body></html>"))
        self.allergieComboBox.setItemText(1, _translate("FicheMed", "CHLOROQUINE"))
        self.allergieComboBox.setItemText(2, _translate("FicheMed", "FRUITS"))
        self.allergieComboBox.setItemText(3, _translate("FicheMed", "NOISETTES"))
        self.allergieComboBox.setItemText(4, _translate("FicheMed", "PIQURES"))
        self.comboBox_medTrait.setItemText(1, _translate("FicheMed", "DR JOSUE"))
        self.comboBox_medTrait.setItemText(2, _translate("FicheMed", "DR GAËL"))
        self.comboBox_medTrait.setItemText(3, _translate("FicheMed", "DR IBRAHIM"))
        self.comboBox_medTrait.setItemText(4, _translate("FicheMed", "DR SILVA"))
        self.serviceComboBox.setItemText(1, _translate("FicheMed", "PEDIATRIE"))
        self.serviceComboBox.setItemText(2, _translate("FicheMed", "OLPHTALMOMOGIE"))
        self.serviceComboBox.setItemText(3, _translate("FicheMed", "GYNECOLOGIE"))
        self.serviceComboBox.setItemText(4, _translate("FicheMed", "URGENCE"))
        self.groupBox_4.setTitle(_translate("FicheMed", "Observations"))
        self.groupBox_5.setTitle(_translate("FicheMed", "Diagnostic"))
        self.label_2.setText(_translate("FicheMed", "Symptôme:"))
        self.commandLinkButtonOrdonance.setText(_translate("FicheMed", "Prescrire une ordonance médicale"))
        self.pushButtonTerminer.setText(_translate("FicheMed", "Terminer la consultation"))
        self.pushButton.setText(_translate("FicheMed", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FicheMed = QtWidgets.QDialog()
    ui = Ui_FicheMed()
    ui.setupUi(FicheMed)
    FicheMed.show()
    sys.exit(app.exec_())
