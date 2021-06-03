# Signals - 006_signals.py

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ZeroSpinBox(QSpinBox):
    # Initialize the signal out of the constructor - otherwise the member functions can't use it - these are global
    atzero = pyqtSignal(int, int)
    zeros = 0
    nulls = 0

    def __init__(self, parent= None):
        super(ZeroSpinBox, self).__init__(parent)
        self.valueChanged.connect(self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.nulls = 5
            self.atzero.emit(self.zeros, self.nulls)


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Initialize a dial
        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        # Initialize a ZeroSpinBox - a custom SpinBox that you created above
        self.zerospinbox = ZeroSpinBox()

        # Set the layout
        layout = QHBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.zerospinbox)
        self.setLayout(layout)

        # Signals - the slots are inside the connect function
        self.dial.valueChanged.connect(self.zerospinbox.setValue)
        self.zerospinbox.valueChanged.connect(self.dial.setValue)
        # atzero is the signal defined on the top - it's not a valid PyQt event - it's made in class ZeroSpinbox
        self.zerospinbox.atzero.connect(self.announce)

        self.setWindowTitle("Signals and Slots")

    # Define the callback for the ATZERO signal from the ZEROSPINBOX
    def announce(self, zeros, nulls):
        print("ZeroSpinbox has been at zero: " + str(zeros) + " times")
        print("Another parameter that can be passed: " + str(nulls))


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()