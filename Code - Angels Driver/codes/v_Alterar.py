from PyQt5 import QtCore, QtWidgets

class Ui_Alterar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lb_nome = QtWidgets.QLabel(self.frame_2)
        self.lb_nome.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lb_nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.lb_nome.setObjectName("lb_nome")
        self.gridLayout_2.addWidget(self.lb_nome, 0, 0, 1, 1)
        self.ln_nome = QtWidgets.QLineEdit(self.frame_2)
        self.ln_nome.setMaximumSize(QtCore.QSize(250, 30))
        self.ln_nome.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_nome.setObjectName("ln_nome")
        self.gridLayout_2.addWidget(self.ln_nome, 0, 1, 1, 1)
        self.lb_cpf = QtWidgets.QLabel(self.frame_2)
        self.lb_cpf.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lb_cpf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.lb_cpf.setObjectName("lb_cpf")
        self.gridLayout_2.addWidget(self.lb_cpf, 1, 0, 1, 1)
        self.ln_cpf = QtWidgets.QLineEdit(self.frame_2)
        self.ln_cpf.setMaximumSize(QtCore.QSize(250, 30))
        self.ln_cpf.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_cpf.setObjectName("ln_cpf")
        self.gridLayout_2.addWidget(self.ln_cpf, 1, 1, 1, 1)
        self.lb_login = QtWidgets.QLabel(self.frame_2)
        self.lb_login.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lb_login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.lb_login.setObjectName("lb_login")
        self.gridLayout_2.addWidget(self.lb_login, 2, 0, 1, 1)
        self.ln_login = QtWidgets.QLineEdit(self.frame_2)
        self.ln_login.setMaximumSize(QtCore.QSize(250, 30))
        self.ln_login.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_login.setObjectName("ln_login")
        self.gridLayout_2.addWidget(self.ln_login, 2, 1, 1, 1)
        self.lb_senha = QtWidgets.QLabel(self.frame_2)
        self.lb_senha.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lb_senha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.lb_senha.setObjectName("lb_senha")
        self.gridLayout_2.addWidget(self.lb_senha, 3, 0, 1, 1)
        self.ln_senha = QtWidgets.QLineEdit(self.frame_2)
        self.ln_senha.setMaximumSize(QtCore.QSize(250, 30))
        self.ln_senha.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_senha.setObjectName("ln_senha")
        self.gridLayout_2.addWidget(self.ln_senha, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.bt_salvar = QtWidgets.QPushButton(self.frame_3)
        self.bt_salvar.setMaximumSize(QtCore.QSize(110, 40))
        self.bt_salvar.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: black\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 127);\n"
"    border-color: rgb(0, 0, 127);\n"
"}")
        self.bt_salvar.setObjectName("bt_salvar")
        self.gridLayout.addWidget(self.bt_salvar, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alterar Dados"))
        self.lb_nome.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Nome:</p></body></html>"))
        self.lb_cpf.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CPF:</p></body></html>"))
        self.lb_login.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Login:</p></body></html>"))
        self.lb_senha.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Senha:</p></body></html>"))
        self.bt_salvar.setText(_translate("MainWindow", "SALVAR"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Alterar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
