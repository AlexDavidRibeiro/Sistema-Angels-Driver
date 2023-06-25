from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

from v_Drivers import Ui_Driver
from v_Alterar import Ui_Alterar

class Driver:
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.drive = Ui_Driver()
        self.drive.setupUi(self.MainWindow)
        self.drive.bt_alterar.clicked.connect(self.alterar)
        self.drive.bt_excluir.clicked.connect(self.excluir)
        self.MainWindow.show()

        con = sqlite3.connect('database\AngelsDriver.db') # Conectando com o Banco de Dados

        with con:
            seta = con.cursor()
            sql = "SELECT Nome, CPF, Login FROM Drivers" # SQL para selecionar os elementos da lista
            seta.execute(sql)
            dados = seta.fetchall()

            self.drive.tabela_listar.setRowCount(len(dados)) # Conta quantos elementos possui em cada linha
            self.drive.tabela_listar.setColumnCount(3)       # Quantidade de colunas pré determinadas

            for i in range (0, len(dados)): # Loop que organiza os dados para exibição
                for j in range (0,3):
                    self.drive.tabela_listar.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))

    def alterar(self): # Função OK

        linha = self.drive.tabela_listar.currentRow() # Faz a leitura da linha do elemento
        
        if linha == -1:
            QMessageBox.about(QMessageBox(),"ALERTA","SELECIONE UMA LINHA!")
        
        else:
            global numID
            self.MainWindow = QtWidgets.QMainWindow()
            self.alt = Ui_Alterar()
            self.alt.setupUi(self.MainWindow)
            self.alt.bt_salvar.clicked.connect(self.salvarDados)

            con = sqlite3.connect('database\AngelsDriver.db')

            with con:
                seta = con.cursor()
                sql = "SELECT ID FROM Drivers"
                seta.execute(sql)
                dados = seta.fetchall()
                id = dados[linha][0]     # Armazena o ID da linha selecionada
                sql = "SELECT * FROM Drivers WHERE ID=?" # Seleciona a linha toda pelo ID
                seta.execute(sql,[str(id)])
                driver = seta.fetchall()

                self.alt.ln_nome.setText(str(driver[0][1]))
                self.alt.ln_cpf.setText(str(driver[0][2]))
                self.alt.ln_login.setText(str(driver[0][3]))
                self.alt.ln_senha.setText(str(driver[0][4]))
            numID = id
            self.MainWindow.show()
        
    def excluir(self): # Função OK
        linha = self.drive.tabela_listar.currentRow() # Faz a leitura da linha do elemento
        
        if linha == -1:
            QMessageBox.about(QMessageBox(),"ALERTA","SELECIONE UMA LINHA!")
        
        else:
            resp = QMessageBox.question(QMessageBox(),"Exclusão de Driver","Você gostaria de excluir o Driver?"
                                        ,QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if resp == QMessageBox.Yes:
                con = sqlite3.connect('database\AngelsDriver.db')

                with con:
                    seta = con.cursor()
                    sql = "SELECT ID FROM Drivers"
                    seta.execute(sql)
                    dados = seta.fetchall()
                    id = dados[linha][0]
                    sql = "DELETE FROM Drivers WHERE ID=?"
                    seta.execute(sql,[str(id)])
                    self.drive.tabela_listar.removeRow(linha)
                QMessageBox.information(QMessageBox(),"EXCLUSÃO","Driver excluído com sucesso!")
    
    def salvarDados(self): # Função OK
        global numID

        nome = self.alt.ln_nome.text()      # Altera o nome do elemento
        cpf = self.alt.ln_cpf.text()        # Altera o cpf do elemento
        login = self.alt.ln_login.text()    # Altera o login do elemento
        senha = self.alt.ln_senha.text()    # Altera a senha do elemento

        if nome != "" and cpf != "" and login != "" and senha != "":

            listaEdit = [nome,cpf,login,senha,numID]

            con = sqlite3.connect('database\AngelsDriver.db')

            with con: 
                seta = con.cursor()
                sql = "UPDATE Drivers SET Nome=?, CPF=?, Login=?, Senha=? WHERE ID=?"
                seta.execute(sql,listaEdit) # Executa e armazena as alterações feitas
            QMessageBox.information(QMessageBox(),"ATUALIZAÇÃO","Atualização concluída com sucesso!")
                
        self.MainWindow.close()     # Fecha a janela de alteração

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    sistema = Driver()
    app.exec()