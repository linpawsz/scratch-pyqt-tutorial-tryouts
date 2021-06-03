# 008_dumb_dialogs.py
# Dialog that is not aware of it's surroundings - signals that don't care about passing values
# The different objects don't care about passing values between each other - they're dumb dialogs


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

__appname__ = "Dumb dialogs"


class Program(QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        self.button = QPushButton("Open Dialog")
        self.label1 = QLabel("Label 1 Result")
        self.label2 = QLabel("Label 2 Result")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

        self.button.clicked.connect(self.DialogOpen)

    def DialogOpen(self):
        dialog = Dialog()
        if dialog.exec_():
            self.label1.setText("SpinBox value is: " + str(dialog.spinBox.value()))
            self.label2.setText("Checkbox is: " + str(dialog.checkbox.isChecked()))
            # We can access the values of the Dialog object in this SLOT function because we passed self into DialogOpen
            # self passed into DialogOpen was the Program - the initial program, not the Dialog
        else:
            # This is what happens when you hit Cancel on the new Dialog Box - WHYY??
            QMessageBox.warning(self, __appname__, "Dialog canceled")


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        # Dialog elements
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

        # These two slots - accept and reject - are built into the QDialog class - check the reference
        self.buttonOk.clicked.connect(self.accept)
        self.buttonCancel.clicked.connect(self.reject)


app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()