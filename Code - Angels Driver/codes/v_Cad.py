from PyQt5 import QtCore, QtWidgets

class Ui_Config(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 550)
        MainWindow.setMaximumSize(QtCore.QSize(400, 550))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 75 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-color: color")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.ln_nome = QtWidgets.QLineEdit(self.frame_3)
        self.ln_nome.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ln_nome.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_nome.setObjectName("ln_nome")
        self.gridLayout_4.addWidget(self.ln_nome, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.ln_cpf = QtWidgets.QLineEdit(self.frame_3)
        self.ln_cpf.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ln_cpf.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_cpf.setObjectName("ln_cpf")
        self.gridLayout_4.addWidget(self.ln_cpf, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.ln_login = QtWidgets.QLineEdit(self.frame_3)
        self.ln_login.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ln_login.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_login.setObjectName("ln_login")
        self.gridLayout_4.addWidget(self.ln_login, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)
        self.ln_senha = QtWidgets.QLineEdit(self.frame_3)
        self.ln_senha.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ln_senha.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_senha.setObjectName("ln_senha")
        self.gridLayout_4.addWidget(self.ln_senha, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bt_cadastrar = QtWidgets.QPushButton(self.frame_4)
        self.bt_cadastrar.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_cadastrar.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
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
        self.bt_cadastrar.setObjectName("bt_cadastrar")
        self.gridLayout_2.addWidget(self.bt_cadastrar, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bt_listar = QtWidgets.QPushButton(self.frame_5)
        self.bt_listar.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_listar.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: black\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 170, 0);\n"
"    border-color: rgb(0, 170, 0);\n"
"}")
        self.bt_listar.setObjectName("bt_listar")
        self.gridLayout_3.addWidget(self.bt_listar, 0, 0, 1, 1)
        self.bt_limpar = QtWidgets.QPushButton(self.frame_5)
        self.bt_limpar.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_limpar.setStyleSheet("QPushButton{\n"
"background-color: rgb(220, 220, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
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
        self.bt_limpar.setObjectName("bt_limpar")
        self.gridLayout_3.addWidget(self.bt_limpar, 0, 1, 1, 1)
        self.bt_adm = QtWidgets.QPushButton(self.frame_5)
        self.bt_adm.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_adm.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-color: black\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 170, 0);\n"
"    border-color: rgb(0, 170, 0);\n"
"}")
        self.bt_adm.setObjectName("bt_adm")
        self.gridLayout_3.addWidget(self.bt_adm, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de Cadastro de Drivers"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">CADASTRAR DRIVER</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Nome:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>CPF:</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>LOGIN:</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>SENHA:</p></body></html>"))
        self.bt_cadastrar.setText(_translate("MainWindow", "CADASTRAR"))
        self.bt_listar.setText(_translate("MainWindow", "LISTAR"))
        self.bt_limpar.setText(_translate("MainWindow", "Limpar Placas"))
        self.bt_adm.setText(_translate("MainWindow", "ADM"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Config()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
