# https://www.youtube.com/watch?v=umU9VP_uX34&list=PLA955A8F9A95378CE&index=14

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import main_ui_MainDialog


class MainDialog(QDialog, main_ui_MainDialog.Ui_Dialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)    # super(<name of the class you just defined>, self ....
        self.setupUi(self)


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()