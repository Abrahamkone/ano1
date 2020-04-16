# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liste_rdv.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_liste_rdv(object):

    def loadData(self):
        from saisie_Id_rdv import ident
        conx = sqlite3.connect('../config/santeplus.db')
        #where id_patient="{}" """.format(ident)
        cur = conx.cursor()
        try:
            cur.execute("""SELECT * FROM rdv where id_patient="{}" """.format(ident))
            print("SQL -->ok")
        except Exception as e:
            print("error here:",e)
        res = cur.fetchall()
        print("len = ",len(res))
        for row_number, row_data in enumerate(res):
            self.liste_rdv_2.setRowCount((row_number+1))
            for column_number, data in enumerate(row_data):
                self.liste_rdv_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conx.close()

    def setupUi(self, liste_rdv):
        liste_rdv.setObjectName("liste_rdv")
        liste_rdv.resize(656, 236)
        self.centralwidget = QtWidgets.QWidget(liste_rdv)
        self.centralwidget.setObjectName("centralwidget")
        self.liste_rdv_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.liste_rdv_2.setGeometry(QtCore.QRect(80, 20, 491, 181))
        self.liste_rdv_2.setObjectName("liste_rdv_2")
        self.liste_rdv_2.setColumnCount(7)
        self.liste_rdv_2.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste_rdv_2.setHorizontalHeaderItem(6, item)
        liste_rdv.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(liste_rdv)
        self.statusbar.setObjectName("statusbar")
        liste_rdv.setStatusBar(self.statusbar)

        self.retranslateUi(liste_rdv)
        QtCore.QMetaObject.connectSlotsByName(liste_rdv)
        self.loadData()

    def retranslateUi(self, liste_rdv):
        _translate = QtCore.QCoreApplication.translate
        liste_rdv.setWindowTitle(_translate("liste_rdv", "Liste des patients"))
        item = self.liste_rdv_2.horizontalHeaderItem(0)
        item.setText(_translate("liste_rdv", "id"))
        item = self.liste_rdv_2.horizontalHeaderItem(1)
        item.setText(_translate("liste_rdv", "Numero Patient"))
        item = self.liste_rdv_2.horizontalHeaderItem(2)
        item.setText(_translate("liste_rdv", "Date Consultation"))
        item = self.liste_rdv_2.horizontalHeaderItem(3)
        item.setText(_translate("liste_rdv", "Heure de Consultation"))
        item = self.liste_rdv_2.horizontalHeaderItem(4)
        item.setText(_translate("liste_rdv", "Medecin"))
        item = self.liste_rdv_2.horizontalHeaderItem(5)
        item.setText(_translate("liste_rdv", "Service"))
        item = self.liste_rdv_2.horizontalHeaderItem(6)
        item.setText(_translate("liste_rdv", "Date RDV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    liste_rdv = QtWidgets.QMainWindow()
    ui = Ui_liste_rdv()
    ui.setupUi(liste_rdv)
    liste_rdv.show()
    ui.loadData()
    sys.exit(app.exec_())
