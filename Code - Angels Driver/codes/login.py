from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sqlite3

from v_Login import Ui_Login
from iniciar import Iniciar

class Login:
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.MainWindow)
        self.ui.bt_entrar.clicked.connect(self.login)
        self.MainWindow.show()

    def driver(self):  # Função para verificação de usuário comum
                
        logar = self.ui.ln_login.text()     # Variável que recebe a string do login
        password = self.ui.ln_senha.text()  # Variável que recebe a string da senha
        log = [logar]                       # Lista que recebe a variável "logar"

        con = sqlite3.connect('database\AngelsDriver.db')  # Conectando com o Banco de Dados

        with con:
            vazio = []  # Lista vazia para verificação se o BD não está vazio
            seta = con.cursor()
            sql = "SELECT Login FROM Drivers"
            seta.execute(sql)
            usuario = seta.fetchall()

            if usuario != vazio:  # Verificação para caso o BD não esteja vazio

                sql = "SELECT Senha FROM Drivers WHERE Login=?"
                seta.execute(sql,log)
                driver = seta.fetchall()

                if usuario[0][0] != logar:  # Verifica se o usuário existe
                    QMessageBox.warning(QMessageBox(),"ALERTA","USUÁRIO NÃO ENCONTRADO!")
                                        
                elif password == driver[0][0]:  # Verifica se a senha do usuário corresponde
                    Iniciar.startup(1)
                    self.sistema = Iniciar()
                    print("Driver Logado")
                    self.MainWindow.close()
                else:
                    QMessageBox.warning(QMessageBox(),"ALERTA","SENHA INVÁLIDA!")
            else:
                QMessageBox.warning(QMessageBox,"ALERTA","NÃO EXISTE USUÁRIO CADASTRADO!\nENTRE EM CONTATO COM SEU ADMINISTRADOR!")

    def login(self): # Função OK

        logar = self.ui.ln_login.text()      # Variável que recebe a string do login
        password = self.ui.ln_senha.text()   # Variável que recebe a string da senha
        log = [logar,password]               # Lista que recebe as variáveis

        con = sqlite3.connect('database\AngelsDriver.db') # Conectando com o Banco de Dados

        if logar != "" and password != "":

            with con:
                seta = con.cursor()
                sql = "SELECT LoginADM, SenhaADM FROM ADM"
                seta.execute(sql)
                dados = seta.fetchall()
                    
                if dados[0][0] == log[0] and dados[0][1] == log[1]:
                    Iniciar.startup(0)
                    self.sistema = Iniciar()
                    print("Administrador Logado")
                    self.MainWindow.close()
                else:
                    self.driver() # Caso NÃO seja ADM, chama a função driver acima.
        else:
            QMessageBox.warning(QMessageBox(),"ATENÇÃO AOS CAMPOS","PREENCHA OS CAMPOS VAZIOS!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    sistema = Login()
    app.exec()