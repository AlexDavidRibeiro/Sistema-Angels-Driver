from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QMessageBox
#import sqlite3

from v_Alerta import Ui_Alerta
from sos import Sos

class Alerta:
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.alert = Ui_Alerta()
        self.alert.setupUi(self.MainWindow)
        self.alert.bt_socorro.clicked.connect(self.socorro)
        self.alert.bt_cancelar.clicked.connect(self.cancelar)
        self.MainWindow.show()

    def placa():
        pass

    def tempo():
        pass

    def fotoCar():
        pass

    def socorro(self): # Função OK
        self.sistema = Sos()
        print("Socorro Chamado")

    def vigiar():
        pass

    def cancelar(self): # Função OK
        self.MainWindow.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    sistema = Alerta()
    app.exec()