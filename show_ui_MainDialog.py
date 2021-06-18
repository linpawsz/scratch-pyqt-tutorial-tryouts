# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\**\PycharmProjects\scratch-pyqt-tutorial-tryouts\show.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(316, 112)
        self.nameEdit = QtWidgets.QLineEdit(MainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(30, 40, 141, 31))
        self.nameEdit.setText("")
        self.nameEdit.setObjectName("nameEdit")
        self.showButton = QtWidgets.QPushButton(MainDialog)
        self.showButton.setGeometry(QtCore.QRect(190, 40, 91, 31))
        self.showButton.setObjectName("showButton")

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)
        MainDialog.setTabOrder(self.showButton, self.nameEdit)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Main Dialog"))
        self.nameEdit.setPlaceholderText(_translate("MainDialog", "What is your name?"))
        self.showButton.setText(_translate("MainDialog", "Show!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainDialog = QtWidgets.QDialog()
    ui = Ui_MainDialog()
    ui.setupUi(MainDialog)
    MainDialog.show()
    sys.exit(app.exec_())

