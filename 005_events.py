# Events - 005_events.py
# Event handling with PyQt

# Signals come out from all QWidgets - unhandled signals are discarded - signals need SLOTS (callable functions)
# Slots need to be defined to handle signals - they need to be defined within the class that's the main design

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dial = QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        # Signals - the slots are inside the connect function
        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

        self.setWindowTitle("Signals and Slots")


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()