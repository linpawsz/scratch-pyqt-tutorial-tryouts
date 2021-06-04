# 009_standard_dialogs.py

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


__appname__ = "Standard dialogs"


class Program(QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        self.button = QPushButton("Open Dialog")
        self.mainSpinBox = QSpinBox()
        self.mainCheckBox = QCheckBox("Main Checkbox value")

        layout = QVBoxLayout()
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckBox)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.DialogOpen)

    def DialogOpen(self):
        # We are going to pass initValues into the Dialog object constructor which is initialized when it's made
        initValues = {"mainSpinBox": self.mainSpinBox.value(), "mainCheckBox": self.mainCheckBox.isChecked()}
        dialog = Dialog(initValues)
        if dialog.exec_():
            self.mainSpinBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkbox.isChecked())
        else:
            # Even when you hit Cancel on your Dialog - it shows this!
            print("didn't work")


class Dialog(QDialog):
    def __init__(self, initvalues, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        # Dialog elements - declarations
        self.checkbox = QCheckBox("Check me out")
        self.spinBox = QSpinBox()
        self.buttonOk = QPushButton("Ok")
        self.buttonCancel = QPushButton("Cancel")

        # Setting the Grid Layout
        layout = QGridLayout()
        layout.addWidget(self.spinBox, 0, 0)
        layout.addWidget(self.checkbox, 0, 1)
        # Let Qt decide where to put the buttons - it can change it's position in the bottom
        layout.addWidget(self.buttonOk)
        layout.addWidget(self.buttonCancel)
        self.setLayout(layout)

        # Didn't pay attention to setChecked - for checkbox - so had to debug the whole thing with try/except
        try:
            self.spinBox.setValue(initvalues['mainSpinBox'])
            self.checkbox.setChecked(initvalues['mainCheckBox'])
        except Exception as e:
            print(e.args)

        # These two slots - accept and reject - are built into the QDialog class - check the reference
        self.buttonOk.clicked.connect(self.accept)
        self.buttonCancel.clicked.connect(self.reject)

    # Over-riding the accept function of the buttons
    def accept(self):

        class GreaterThanFive(Exception): pass
        class IsZero(Exception): pass

        try:
            if self.spinBox.value() > 5:
                raise GreaterThanFive("The SpinBox value cannot be greater than 5")
            elif self.spinBox.value() == 0:
                raise IsZero("The SpinBox value cannot be equal to 0")
            else:
                QDialog.accept(self)

        except GreaterThanFive as e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return

        except IsZero as e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return

    #def reject(self):


app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()