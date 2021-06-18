Qt Designer Notes
----------------

https://www.youtube.com/watch?v=u0zhLEHHZBU&list=PLA955A8F9A95378CE&index=11  
  
Slots and Signals can be set in the designer itself  
- QLabel and LineEdit example  
- Either through Edit Slots and Actions Tab, or through Slot/Action Editor Window  
  
  
Property editors  
- This one shows the class inheritance from top to bottom - QObject, QWidget, QDialog
  
  
Tab order management throughout the application   
- Just click and set the order - that's simple  
  
  
Integrate Qt-Designer output file of the UI - and integrate it into PyQt code  
- PyQt doesn't have the luxury of editing code in the UI designer itself  
- But don't complain - this is easy  

Place holder text in the LineEdit QWidget - the text goes away when you click on it

  
Convert .ui file into .py file - and then you have to import the .py file into your PyQt code  
- uic.exe show.ui -o showGui.py  
- Command on system:  
- C:\Users\**\anaconda3\Library\bin>pyuic5.bat -x C:\Users\**\PycharmProjects\scratch-pyqt-tutorial-tryouts\show.ui -o C:\Users\**\PycharmProjects\scratch-pyqt-tutorial-tryouts\show_ui_MainDialog.py    
- Had to install "python.exe -m pip install pyqt5-tools"  
- This also install Qt-Designer - it's own version and type - not the binary you installed  
- More methods - https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html  


