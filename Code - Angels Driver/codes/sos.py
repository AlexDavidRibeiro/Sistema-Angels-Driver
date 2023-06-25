from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QMessageBox
#import sqlite3

from v_Sos import Ui_Sos

class Sos:
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.soc = Ui_Sos()
        self.soc.setupUi(self.MainWindow)
        #self.soc.bt_entrar.clicked.connect(self.login)
        self.MainWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    sistema = Sos()
    app.exec()