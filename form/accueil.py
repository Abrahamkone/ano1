# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accueil.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from consul import Ui_Consultation
from saisie_Id import Ui_SaisieId
from inscrit import Ui_Inscrit
from PyQt5.QtWidgets import QMessageBox

class Ui_Accueil(object):
    def overture_de_fenetre_inscrit(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_Inscrit()
        self.ui.setupUi(self.Window)
        self.Window.show()

    def overture_de_fenetre_saisie_id(self):
        #no touch
        self.Window = QtWidgets.QMainWindow()
        #Ui_saisieId varie selon la fenetre qu'on veut afficher
        self.ui = Ui_SaisieId()
        self.ui.setupUi(self.Window)
        #juste pour faire disparaitre la fenetre courante
        #devine(:
        self.Window.show()


    def fonctionClickSupprimer(self):
        buttonReponse = QMessageBox.question(self, 'Attention ! ', 'Voulez vous vraiment Supprimer ?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # if buttonReponse == QMessageBox.Yes:
            # self.line_Edit_Supprimer.clear()
            # print('Suppression de id : ', line_Edit_Supprimer.text())
        # else:
            # print('Suppression Annulée !')

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
        self.groupe_Affiche_Fiche = QtWidgets.QGroupBox(self.centralwidget)
        self.groupe_Affiche_Fiche.setGeometry(QtCore.QRect(10, 380, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupe_Affiche_Fiche.setFont(font)
        self.groupe_Affiche_Fiche.setObjectName("groupe_Affiche_Fiche")
        self.line_Edit_Afficher_2 = QtWidgets.QLineEdit(
            self.groupe_Affiche_Fiche)
        self.line_Edit_Afficher_2.setGeometry(QtCore.QRect(10, 50, 181, 20))
        self.line_Edit_Afficher_2.setObjectName("line_Edit_Afficher_2")
        self.boutton_Afficher_fiche = QtWidgets.QPushButton(
            self.groupe_Affiche_Fiche)
        self.boutton_Afficher_fiche.setGeometry(QtCore.QRect(60, 80, 81, 31))
        self.boutton_Afficher_fiche.setObjectName("boutton_Afficher_fiche")
        self.groupe_Modifier_Fiche = QtWidgets.QGroupBox(self.centralwidget)
        self.groupe_Modifier_Fiche.setGeometry(
            QtCore.QRect(230, 380, 221, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupe_Modifier_Fiche.setFont(font)
        self.groupe_Modifier_Fiche.setObjectName("groupe_Modifier_Fiche")
        self.line_Edit_Modiffier = QtWidgets.QLineEdit(
            self.groupe_Modifier_Fiche)
        self.line_Edit_Modiffier.setGeometry(QtCore.QRect(12, 50, 191, 20))
        self.line_Edit_Modiffier.setObjectName("line_Edit_Modiffier")
        self.boutton_Modiffierr_fiche = QtWidgets.QPushButton(
            self.groupe_Modifier_Fiche)
        self.boutton_Modiffierr_fiche.setGeometry(
            QtCore.QRect(60, 80, 101, 31))
        self.boutton_Modiffierr_fiche.setObjectName("boutton_Modiffierr_fiche")
        self.groupe_Supprimer_Fiche = QtWidgets.QGroupBox(self.centralwidget)
        self.groupe_Supprimer_Fiche.setGeometry(
            QtCore.QRect(460, 380, 221, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupe_Supprimer_Fiche.setFont(font)
        self.groupe_Supprimer_Fiche.setObjectName("groupe_Supprimer_Fiche")
        self.line_Edit_Supprimer = QtWidgets.QLineEdit(
            self.groupe_Supprimer_Fiche)
        self.line_Edit_Supprimer.setGeometry(QtCore.QRect(12, 50, 191, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 13, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 43, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 6, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 8, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 13, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 134, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 13, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 43, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 6, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 8, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 13, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 134, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 6, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 13, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 43, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 6, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 8, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 6, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(104, 6, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 13, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 13, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(209, 13, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipText, brush)
        self.line_Edit_Supprimer.setPalette(palette)
        self.line_Edit_Supprimer.setObjectName("line_Edit_Supprimer")
        self.boutton_Supprimer_fiche = QtWidgets.QPushButton(
            self.groupe_Supprimer_Fiche)
        self.boutton_Supprimer_fiche.setGeometry(QtCore.QRect(54, 80, 101, 31))
        self.boutton_Supprimer_fiche.setObjectName("boutton_Supprimer_fiche")
        self.boutton_Inscription = QtWidgets.QPushButton(self.centralwidget)
        self.boutton_Inscription.setGeometry(QtCore.QRect(30, 150, 171, 71))
        self.boutton_Inscription.setObjectName("boutton_Inscription")
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
        Accueil.setTabOrder(self.pushButton, self.pushButton_2)

        #le boutton a pour nom : pushbutton et la metode overture_de_fenetre_consul est define en haut
        # son role : au clic, une connexion est faite avec la methode qui s'execute
        self.pushButton.clicked.connect(self.overture_de_fenetre_saisie_id)
        # le nom du bouton : pushButton_2  = ouvre la fenetre saisie de id (:
        self.pushButton_2.clicked.connect(self.overture_de_fenetre_saisie_id)
        self.boutton_Inscription.clicked.connect(
            self.overture_de_fenetre_inscrit)

        # pour Supprimer
        self.boutton_Supprimer_fiche.clicked.connect(
            self.fonctionClickSupprimer)

    def retranslateUi(self, Accueil):
        _translate = QtCore.QCoreApplication.translate
        Accueil.setWindowTitle(_translate("Accueil", "Accueil"))
        self.acceul.setText(_translate(
            "Accueil", "ACCEUIL Hopital Santé du Bonheur"))
        self.pushButton.setText(_translate("Accueil", "Consultation"))
        self.pushButton_2.setText(_translate("Accueil", "Rendez-vous"))
        self.label_2.setText(_translate(
            "Accueil", "bonjour Mr ou Mme vous êtes venus pour ?"))
        self.groupe_Affiche_Fiche.setTitle(
            _translate("Accueil", "Afficher La Fiche"))
        self.line_Edit_Afficher_2.setPlaceholderText(
            _translate("Accueil", "Numero Unique"))
        self.boutton_Afficher_fiche.setText(_translate("Accueil", "Afficher"))
        self.groupe_Modifier_Fiche.setTitle(
            _translate("Accueil", "Modiffier la fiche"))
        self.line_Edit_Modiffier.setPlaceholderText(
            _translate("Accueil", "Numero Unique"))
        self.boutton_Modiffierr_fiche.setText(
            _translate("Accueil", "Modiffier"))
        self.groupe_Supprimer_Fiche.setTitle(
            _translate("Accueil", "Supprimer La fiche"))
        self.line_Edit_Supprimer.setPlaceholderText(
            _translate("Accueil", "Numero Unique"))
        self.boutton_Supprimer_fiche.setText(
            _translate("Accueil", "Supprimer"))
        self.boutton_Inscription.setText(_translate("Accueil", "Inscription"))
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
