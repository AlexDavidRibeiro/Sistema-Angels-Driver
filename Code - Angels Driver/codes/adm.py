from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

from v_ADM import Ui_Adm

class Adm:
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.admin = Ui_Adm()
        self.admin.setupUi(self.MainWindow)
        self.admin.bt_salvar.clicked.connect(self.salvar)
        self.admin.bt_propri.clicked.connect(self.propri)
        self.MainWindow.show()

        con = sqlite3.connect('database\AngelsDriver.db')

        with con:
            seta = con.cursor()
            sql = "SELECT * FROM ADM"
            seta.execute(sql)
            admin = seta.fetchall()

            self.admin.ln_nomeADM.setText(str(admin[0][0]))
            self.admin.ln_loginADM.setText(str(admin[0][1]))
            self.admin.ln_senhaADM.setText(str(admin[0][2]))
            self.admin.ln_empresa.setText(str(admin[0][3]))

    def propri(self): # Função OK
        con = sqlite3.connect('database\AngelsDriver.db')

        with con:
            seta = con.cursor()
            sql = "SELECT * FROM ADM"
            seta.execute(sql)
            admin = seta.fetchall()

        QMessageBox.information(QMessageBox(),"Informações do Administrador","Sistema Angel's Driver\n"
                                f"Licenciado para {admin[0][3]}\n"
                                "Sob a licença: SAD01.30.23.RCorp.\n"
                                "Versão do Sistema 3.0")

    def salvar(self): # Função Ok
        nome = self.admin.ln_nomeADM.text()
        login = self.admin.ln_loginADM.text()
        senha = self.admin.ln_senhaADM.text()
        empresa = self.admin.ln_empresa.text()

        data = [nome,login,senha,empresa]

        resp = QMessageBox.question(QMessageBox(),"ATENÇÃO - ALTERAÇÃO DE CADASTRO DO ADMINISTRADOR","Deseja realmente alterar os dados do administrador?",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if resp == QMessageBox.Yes:
            con = sqlite3.connect('database\AngelsDriver.db')
                
            with con:
                seta = con.cursor()
                sql = "UPDATE ADM SET NomeADM=?, LoginADM=?, SenhaADM=?, Empresa=?"
                seta.execute(sql,data)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    sistema = Adm()
    app.exec()