# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liste_rdv.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_liste_rdv(object):
    def setupUi(self, liste_rdv):
        liste_rdv.setObjectName("liste_rdv")
        liste_rdv.resize(656, 236)
        self.centralwidget = QtWidgets.QWidget(liste_rdv)
        self.centralwidget.setObjectName("centralwidget")
        self.liste_rdv_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.liste_rdv_2.setGeometry(QtCore.QRect(80, 20, 491, 181))
        self.liste_rdv_2.setObjectName("liste_rdv_2")
        self.liste_rdv_2.setColumnCount(4)
        self.liste_rdv_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(3, item)
        liste_rdv.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(liste_rdv)
        self.statusbar.setObjectName("statusbar")
        liste_rdv.setStatusBar(self.statusbar)

        self.retranslateUi(liste_rdv)
        QtCore.QMetaObject.connectSlotsByName(liste_rdv)

    def retranslateUi(self, liste_rdv):
        _translate = QtCore.QCoreApplication.translate
        liste_rdv.setWindowTitle(_translate("liste_rdv", "Liste des patients"))
        item = self.liste_rdv_2.horizontalHeaderItem(0)
        item.setText(_translate("liste_rdv", "Date de consultation"))
        item = self.liste_rdv_2.horizontalHeaderItem(1)
        item.setText(_translate("liste_rdv", "Heure"))
        item = self.liste_rdv_2.horizontalHeaderItem(2)
        item.setText(_translate("liste_rdv", "Nom du medecin"))
        item = self.liste_rdv_2.horizontalHeaderItem(3)
        item.setText(_translate("liste_rdv", "Date de rendez-vous"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    liste_rdv = QtWidgets.QMainWindow()
    ui = Ui_liste_rdv()
    ui.setupUi(liste_rdv)
    liste_rdv.show()
    sys.exit(app.exec_())
