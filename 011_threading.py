# Copied from 010_incorporating_ui_code_into_python_code
# https://www.youtube.com/watch?v=eD91nE8q8Nk&list=PLA955A8F9A95378CE&index=12

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import show_ui_MainDialog
import time


# Inherits two base classes - interesting!
class MainDialog(QDialog, show_ui_MainDialog.Ui_MainDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)    # super(<name of the class you just defined>, self ....
        self.setupUi(self)

        self.showButton.setText("Process")
        # self.Widget.Action/Slot.connect(other widget) - inherited showButton from the Qt-Designed show_ui_MainDialog
        self.showButton.clicked.connect(self.processData)
        # This will hang the UI - until the processData is done

        self.workerThread = WorkerThread()
        self.workerThread.my_signal.connect(self.threadDone, Qt.DirectConnection)

    def processData(self):

        self.workerThread.start()  # this calls your run() overridden function
        # You also need wake, terminate methods - but Python handles it well - so we don't use it here right now

        # We're gonna simulate a 5 second delay - coz the process is happening - some form of code suspension
        # anticipating response from a server - wait for a server to respond with the result of your query
        # time.sleep(5)
        QMessageBox.information(self, "Done!", "Done")

    # We can even pass a piece of string from the signal - using str here instead of QString - coz I can't find it
    def threadDone(self, text):
        # self.nameEdit.setText("Worker thread finished processing")
        self.nameEdit.setText(text)
        print(text)


# Communicating between two threads can be tricky
# Your application can bug out if you don't carefully design your software
class WorkerThread(QThread):
    my_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)

    # Overriding the built-in method run
    def run(self):
        time.sleep(5)
        self.my_signal.emit("Confirmation that the thread is finished...")  # Qt.DirectConnection - doesn't matter what int you pass in emit - makes no sense
        print("Done with the thread.")


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
