# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\saisie_Id.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaisieId(object):
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
        self.id_Patient = QtWidgets.QTextBrowser(SaisieId)
        self.id_Patient.setGeometry(QtCore.QRect(70, 110, 291, 31))
        self.id_Patient.setMouseTracking(True)
        self.id_Patient.setFocusPolicy(QtCore.Qt.StrongFocus)
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

    def retranslateUi(self, SaisieId):
        _translate = QtCore.QCoreApplication.translate
        SaisieId.setWindowTitle(_translate("SaisieId", "Saisie du Numero Unique"))
        self.label.setText(_translate("SaisieId", "Numero Unique"))
        self.boutton_Valider_Id.setText(_translate("SaisieId", "Valider"))
        self.button_Annuler_Id.setText(_translate("SaisieId", "Annuler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SaisieId = QtWidgets.QDialog()
    ui = Ui_SaisieId()
    ui.setupUi(SaisieId)
    SaisieId.show()
    sys.exit(app.exec_())
