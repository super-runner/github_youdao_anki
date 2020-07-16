import sys
from PyQt5 import QtWidgets, uic
from convertor_cli import parseEngine
from dialog import Ui_Dialog

class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    if window.exec() == 1:
        xmlPath = window.plainTextEdit.toPlainText()
        parseEngine (xmlPath.strip())
    