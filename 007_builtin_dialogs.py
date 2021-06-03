# Built-in dialogs - 007_builtin_dialogs.py
# GOAL: We need to figure out more ways to open Dialogs and Forms from one of the Forms

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

__appname__ = "Seventh video"


class Program(QDialog):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.openButton = QPushButton("Open")
        self.saveButton = QPushButton("Save")
        self.beerButton = QPushButton("Beer")
        self.closeButton = QPushButton("Close")

        # Be careful not to type in self.open() - coz we're not calling the function
        # We're just specifying a function caller
        self.openButton.clicked.connect(self.open)
        self.saveButton.clicked.connect(self.save)
        # self.beerButton.clicked.connect(self.beer)
        self.closeButton.clicked.connect(self.close)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.openButton)
        layout.addWidget(self.saveButton)
        layout.addWidget(self.beerButton)
        layout.addWidget(self.closeButton)
        self.setLayout(layout)

    def open(self):
        dir = "."
        fileObj = QFileDialog.getOpenFileName(self, __appname__ + "Open File Dialog", dir, filter="Text Files (*.txt)")
        print(fileObj, type(fileObj))
        filename = fileObj[0]
        file = open(filename, "r")
        read = file.read()
        file.close()
        print(read)

    def save(self):
        dir = "."
        fileObj = QFileDialog.getSaveFileName(self, "Save this file whaaaa", dir, filter="Text Files (*.txt)")
        print(fileObj, type(fileObj))
        contents = "Hello from this YouTube tutorial PythonBo"
        filename = fileObj[0]
        open(filename, mode="w").write(contents)

    # def beer(self):
    #     message = "Who has a beer button on the computer ... no we're not getting you beer"
    #     DialogBox = QDialog(message)
    #     DialogBox.show()

    def close(self):
        sys.exit()


app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()