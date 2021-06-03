# Currency converter - doesn't work - needs rework - where to get currency data - how to work with it

import sys
import urllib3
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.getdate()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 1000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        # self.toComboBox.additems(rates)           # Figure out how to write it here
        self.toLabel = QLabel("1.00")

        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

        # The IDE get's massively confused with the below statement - keep faith and continue writing code
        self.fromComboBox.currentIndexChanged.connect(self.updateUi)
        self.toComboBox.currentIndexChanged.connect(self.updateUi)
        self.fromSpinBox.valueChanged.connect(self.updateUi)

    def updateUi(self):
        to = self.toComboBox.currentText()
        # reserved keyword from_
        from_ = self.fromComboBox.currentText()

        amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
        self.toLabel.setText("%0.2f" % amount)

    def getdate(self):
        self.rates = {}

        try:
            date = "Unknown"

            # We need to figure out another way to get currency exchange data and play with it - here's the skeleton
            # http = urllib3.PoolManager()
            # url = "http://www.bankofcanada.ca/en/markets/csv/exchange_end.csv"
            # response = http.request('GET', url)

            for line in fh:
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing")):
                    continue
                fields = line.split(",")
                if line.startswith("Date"):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass
            return "Exchange rates date: " + date
        except Exception as e:
            return "Failed to download: \n%s" % e.args


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
