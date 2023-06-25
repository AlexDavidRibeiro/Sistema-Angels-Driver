from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

from v_Cad import Ui_Config
from adm import Adm
from driver import Driver

class Config:
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.conf = Ui_Config()
        self.conf.setupUi(self.MainWindow)
        self.conf.bt_adm.clicked.connect(self.adm)
        self.conf.bt_listar.clicked.connect(self.listar)
        self.conf.bt_cadastrar.clicked.connect(self.cadastrar)
        self.conf.bt_limpar.clicked.connect(self.limpar)
        self.MainWindow.show()

    def cadastrar(self): # Função OK
        nome = self.conf.ln_nome.text()
        cpf = self.conf.ln_cpf.text()
        login = self.conf.ln_login.text()
        senha = self.conf.ln_senha.text()

        if nome != "" or cpf != "" or login != "" or senha != "":  

            data = [nome,cpf,login,senha]
            
            con = sqlite3.connect('database\AngelsDriver.db')
            
            with con:
                seta = con.cursor()
                sql = "INSERT INTO Drivers (Nome, CPF, Login, Senha) VALUES (?,?,?,?)"
                seta.execute(sql,data)

                QMessageBox.information(QMessageBox(),"Cadastro de Driver",f"Driver {data[0]} cadastrado com sucesso!")

            nome = self.conf.ln_nome.setText("")
            cpf = self.conf.ln_cpf.setText("")
            login = self.conf.ln_login.setText("")
            senha = self.conf.ln_senha.setText("")

        else:
            QMessageBox.warning(QMessageBox(),"ALERTA","Ainda existem campos vazios.")

    def adm(self): # Função OK
        self.sistema = Adm()

    def listar(self): # Função OK
        self.sistema = Driver()
    
    def limpar(self): # Função OK
        con = sqlite3.connect('database\AngelsDriver.db')

        with con:
            seta = con.cursor()
            sql = "SELECT * FROM Placas"
            seta.execute(sql)
            dados = seta.fetchall()
                        
            if dados == []:
                QMessageBox.warning(QMessageBox(),"ATENÇÃO","Não existem PLACAS REGISTRADAS")
            else:
                sql = "DELETE FROM Placas"
                seta.execute(sql)
                QMessageBox.information(QMessageBox(),"EXCLUSÃO DE PLACAS","Limpeza das PLACAS completa!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    sistema = Config()
    app.exec()