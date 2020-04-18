# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accueil.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


iden = "none"


class Ui_Accueil(object):

    def btn_modifier(self):
        from modif import Ui_Modif
        global iden
        iden = self.line_Edit_Modiffier.text()
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_Modif()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def send_iden(self):
        global iden
        iden = self.line_Edit_Modiffier.text()
        print("id_p dans la fonction =", iden)

    def overture_de_fenetre_inscrit(self):
        from inscrit import Ui_Inscrit
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_Inscrit()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def overture_de_fenetre_modif(self):
        from modif import Ui_Modif
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_Modif()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def overture_de_fenetre_saisie_id(self):
        from saisie_Id import Ui_SaisieId
        # no touch
        self.Window = QtWidgets.QMainWindow()
        # Ui_saisieId varie selon la fenetre qu'on veut afficher
        self.ui = Ui_SaisieId()
        self.ui.setupUi(self.Window)
        # juste pour faire disparaitre la fenetre courante
        # devine(:
        self.Window.show()

    def overture_de_fenetre_saisie_id_rdv(self):
        from saisie_Id_rdv import Ui_SaisieId_rdv
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_SaisieId_rdv()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def open_liste_patient(self):
        from liste import Ui_liste
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_liste()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def open_liste_rdv_aff(self):
        from liste_rdv_aff import Ui_liste
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_liste()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def delete_info(self):
        from Database import connexion
        num = self.line_Edit_Supprimer.text()
        conx, cur = connexion()

        try:
            cur.execute("""SELECT * FROM patient WHERE id_patient="{}" """.format(num))
        except Exception as e:
            print("ERREUR SELECTION TABLE patient: ", e)

        res = cur.fetchall()
        if(len(res) != 0):

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Alert")
            msgBox.setText("Voulez vous vraiment supprimer le patient N° {}".format(num))
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec_()

            if returnValue == QMessageBox.Yes:
                try:
                    cur.execute("""DELETE FROM patient WHERE id_patient="{}" """.format(num))
                    cur.execute("""DELETE FROM rdv WHERE id_patient="{}" """.format(num))
                    conx.commit()
                    print("SQL SUPPRESSION TABLE patient --> ok")
                    msg = QMessageBox()
                    msg.setWindowTitle("Info")
                    msg.setText("Effacé avec success!!!")
                    msg.exec_()
                    conx.close()
                except Exception as e:
                    print("ERREUR SUPPRESSION TABLE patient: ", e)
                    conx.close()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Alert")
            msg.setText("Le patient n'existe pas dans la base de donnée!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def setupUi(self, Accueil):
        Accueil.setObjectName("Accueil")
        Accueil.resize(691, 531)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        Accueil.setFont(font)
        Accueil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(Accueil)
        self.centralwidget.setObjectName("centralwidget")
        self.acceul = QtWidgets.QLabel(self.centralwidget)
        self.acceul.setGeometry(QtCore.QRect(100, 40, 511, 41))
        self.acceul.setObjectName("acceul")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 200, 201, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 140, 191, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 110, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupe_Modifier_Fiche = QtWidgets.QGroupBox(self.centralwidget)
        self.groupe_Modifier_Fiche.setGeometry(QtCore.QRect(70, 380, 221, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupe_Modifier_Fiche.setFont(font)
        self.groupe_Modifier_Fiche.setObjectName("groupe_Modifier_Fiche")
        self.line_Edit_Modiffier = QtWidgets.QLineEdit(self.groupe_Modifier_Fiche)
        self.line_Edit_Modiffier.setGeometry(QtCore.QRect(12, 50, 191, 20))
        self.line_Edit_Modiffier.setObjectName("line_Edit_Modiffier")
        self.boutton_Modiffierr_fiche = QtWidgets.QPushButton(self.groupe_Modifier_Fiche)
        self.boutton_Modiffierr_fiche.setGeometry(QtCore.QRect(60, 80, 101, 31))
        self.boutton_Modiffierr_fiche.setObjectName("boutton_Modiffierr_fiche")
        self.groupe_Supprimer_Fiche = QtWidgets.QGroupBox(self.centralwidget)
        self.groupe_Supprimer_Fiche.setGeometry(QtCore.QRect(410, 380, 221, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupe_Supprimer_Fiche.setFont(font)
        self.groupe_Supprimer_Fiche.setObjectName("groupe_Supprimer_Fiche")
        self.line_Edit_Supprimer = QtWidgets.QLineEdit(self.groupe_Supprimer_Fiche)
        self.line_Edit_Supprimer.setGeometry(QtCore.QRect(12, 50, 191, 20))
        self.line_Edit_Supprimer.setObjectName("line_Edit_Supprimer")
        self.boutton_Supprimer_fiche = QtWidgets.QPushButton(
            self.groupe_Supprimer_Fiche)
        self.boutton_Supprimer_fiche.setGeometry(QtCore.QRect(54, 80, 101, 31))
        self.boutton_Supprimer_fiche.setObjectName("boutton_Supprimer_fiche")
        self.boutton_Inscription = QtWidgets.QPushButton(self.centralwidget)
        self.boutton_Inscription.setGeometry(QtCore.QRect(30, 150, 171, 71))
        self.boutton_Inscription.setObjectName("boutton_Inscription")
        Accueil.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Accueil)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        Accueil.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Accueil)
        self.statusbar.setObjectName("statusbar")
        Accueil.setStatusBar(self.statusbar)
        self.actionListe_des_Patients = QtWidgets.QAction(Accueil)
        self.actionListe_des_Patients.setObjectName("actionListe_des_Patients")
        self.actionListe_des_RDV = QtWidgets.QAction(Accueil)
        self.actionListe_des_RDV.setObjectName("actionListe_des_RDV")
        self.menuOptions.addAction(self.actionListe_des_Patients)
        self.menuOptions.addAction(self.actionListe_des_RDV)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(Accueil)
        QtCore.QMetaObject.connectSlotsByName(Accueil)
        Accueil.setTabOrder(self.pushButton, self.pushButton_2)

        # pour Inscription
        self.boutton_Inscription.clicked.connect(self.overture_de_fenetre_inscrit)

        # pour Consultation
        self.pushButton.clicked.connect(self.overture_de_fenetre_saisie_id)

        # pour Rendez vous
        self.pushButton_2.clicked.connect(self.overture_de_fenetre_saisie_id_rdv)

        # pour Modiffier
        # self.boutton_Modiffierr_fiche.clicked.connect(self.send_iden)
        self.boutton_Modiffierr_fiche.clicked.connect(self.btn_modifier)

        # pour Supprimer
        self.boutton_Supprimer_fiche.clicked.connect(self.delete_info)

        self.actionListe_des_Patients.triggered.connect(self.open_liste_patient)
        self.actionListe_des_RDV.triggered.connect(self.open_liste_rdv_aff)

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "Accueil"))
        self.acceul.setText(_translate(
            "Accueil", "ACCEUIL Hopital Santé du Bonheur"))
        self.pushButton.setText(_translate("Accueil", "Consultation"))
        self.pushButton_2.setText(_translate("Accueil", "Rendez-vous"))
        self.groupe_Modifier_Fiche.setTitle(
            _translate("Accueil", "Modiffier la fiche"))
        self.line_Edit_Modiffier.setPlaceholderText(
            _translate("Accueil", "Numero Unique"))
        self.boutton_Modiffierr_fiche.setText(
            _translate("Accueil", "Modiffier"))
        self.groupe_Supprimer_Fiche.setTitle(
            _translate("Accueil", "Supprimer Patient"))
        self.line_Edit_Supprimer.setPlaceholderText(
            _translate("Accueil", "Numero Unique"))
        self.boutton_Supprimer_fiche.setText(
            _translate("Accueil", "Supprimer"))
        self.boutton_Inscription.setText(_translate("Accueil", "Inscription"))
        self.menuOptions.setTitle(_translate("Accueil", "options"))
        self.actionListe_des_Patients.setText(_translate("Accueil", "Liste des Patients"))
        self.actionListe_des_RDV.setText(_translate("Accueil", "Liste des RDV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accueil = QtWidgets.QMainWindow()
    ui = Ui_Accueil()
    ui.setupUi(Accueil)
    Accueil.show()
    sys.exit(app.exec_())
