# https://www.youtube.com/watch?v=eD91nE8q8Nk&list=PLA955A8F9A95378CE&index=12

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import show_ui_MainDialog


# Inherits two base classes - interesting!
class MainDialog(QDialog, show_ui_MainDialog.Ui_MainDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)    # super(<name of the class you just defined>, self ....
        self.setupUi(self)


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()