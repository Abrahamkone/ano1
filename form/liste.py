# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liste.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_liste(object):

    def loadData(self):
        from Database import connexion
        conx, cur = connexion()
        try:
            cur.execute("""SELECT * FROM patient""")
            print("SQL -->ok")
        except Exception as e:
            print("error here:",e)
        res = cur.fetchall()
        print("len = ",len(res))
        for row_number, row_data in enumerate(res):
            self.tableWidget.setRowCount((row_number+1))
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conx.close()

    def setupUi(self, liste):
        liste.setObjectName("liste")
        liste.resize(759, 571)
        self.centralwidget = QtWidgets.QWidget(liste)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 671, 531))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        liste.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(liste)
        self.statusbar.setObjectName("statusbar")
        liste.setStatusBar(self.statusbar)

        self.retranslateUi(liste)
        QtCore.QMetaObject.connectSlotsByName(liste)
        self.loadData()

    def retranslateUi(self, liste):
        _translate = QtCore.QCoreApplication.translate
        liste.setWindowTitle(_translate("liste", "Liste des patients"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("liste_rdv", "Numero Patient"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("liste_rdv", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("liste_rdv", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("liste_rdv", "Sexe"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("liste_rdv", "Date de Naissance"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("liste_rdv", "CNI"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("liste_rdv", "Profession"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("liste_rdv", "Contact"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("liste_rdv", "Email"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("liste_rdv", "Assurance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    liste = QtWidgets.QMainWindow()
    ui = Ui_liste()
    ui.setupUi(liste)
    liste.show()
    sys.exit(app.exec_())
