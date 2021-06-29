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

"""
https://www.youtube.com/watch?v=nixHrjsezac&list=PLA955A8F9A95378CE&index=15
- this video basically replaces QDialog with QMainWindow and makes an application with toolbars

https://www.youtube.com/watch?v=nixHrjsezac&list=PLA955A8F9A95378CE&index=16
- this one shows the new signal slot method style syntax from the older ones - not that important
- emitting signals is also important - learn about this in detail when using GUI programming
- myOwnSignal = Signal((int,), (str,))  <- use tuples also - this is acceptable - use commas to define tuples
- Check after 20:00 - how to pass multiple parameters for the same signal - multiple signal handlers with tuples 

https://www.youtube.com/watch?v=nixHrjsezac&list=PLA955A8F9A95378CE&index=17
- How to style the objects and buttons - put hues and colors on it - use CSS styling mechanisms - color codes




"""