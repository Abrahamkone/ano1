# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liste.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_liste(object):
    def setupUi(self, liste):
        liste.setObjectName("liste")
        liste.resize(854, 589)
        self.centralwidget = QtWidgets.QWidget(liste)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 671, 531))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
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
        liste.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(liste)
        self.statusbar.setObjectName("statusbar")
        liste.setStatusBar(self.statusbar)

        self.retranslateUi(liste)
        QtCore.QMetaObject.connectSlotsByName(liste)

    def retranslateUi(self, liste):
        _translate = QtCore.QCoreApplication.translate
        liste.setWindowTitle(_translate("liste", "Liste des patients"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("liste", "Date de consultation"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("liste", "Heure"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("liste", "N° de compte"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("liste", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("liste", "Prenom(s)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("liste", "Date de rendez-vous"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    liste = QtWidgets.QMainWindow()
    ui = Ui_liste()
    ui.setupUi(liste)
    liste.show()
    sys.exit(app.exec_())

