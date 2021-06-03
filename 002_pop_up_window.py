# https://www.youtube.com/watch?v=0vvb7Kv59qA&list=PLA955A8F9A95378CE&index=2
# Creating a Pop Up Time Window
# Usage: 002_pop_up_window.py HH:MM <custom message>
# Add the parameters in the configurations if using an IDE.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time


# This is imported from PyQt5.QtWidgets
app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = "Alert!"

    if len(sys.argv) < 2:
        raise ValueError

    hours, minutes = sys.argv[1].split(":")
    due = QTime(int(hours), int(minutes))

    if not due.isValid():
        raise ValueError

    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])

except ValueError:
    message = "Usage: <filename>.py HH:MM [optional message]"

while QTime.currentTime() < due:
    time.sleep(10)


# label just shows something on the GUI element
label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()

# countdown timer, 20000 is SIGNAL, app.quit() is the SLOT/method, this singleshot is a signal function
QTimer.singleShot(10000, lambda: app.quit())
# exec_ is a reserved keyword in python - that's why the _ (underscore)
app.exec_()