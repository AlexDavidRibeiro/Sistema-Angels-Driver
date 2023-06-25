from PyQt5 import QtCore, QtWidgets

class Ui_Adm(object):
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
        self.frame.setStyleSheet("")
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 75 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-color: color")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.ln_nomeADM = QtWidgets.QLineEdit(self.frame_3)
        self.ln_nomeADM.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ln_nomeADM.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_nomeADM.setObjectName("ln_nomeADM")
        self.gridLayout.addWidget(self.ln_nomeADM, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 127);\n"
"font: 75 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.ln_loginADM = QtWidgets.QLineEdit(self.frame_3)
        self.ln_loginADM.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ln_loginADM.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_loginADM.setObjectName("ln_loginADM")
        self.gridLayout.addWidget(self.ln_loginADM, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 127);\n"
"font: 75 12pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.ln_senhaADM = QtWidgets.QLineEdit(self.frame_3)
        self.ln_senhaADM.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ln_senhaADM.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_senhaADM.setObjectName("ln_senhaADM")
        self.gridLayout.addWidget(self.ln_senhaADM, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 127);\n"
"font: 75 12pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.ln_empresa = QtWidgets.QLineEdit(self.frame_3)
        self.ln_empresa.setMaximumSize(QtCore.QSize(16777215, 30))
        self.ln_empresa.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_empresa.setObjectName("ln_empresa")
        self.gridLayout.addWidget(self.ln_empresa, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bt_salvar = QtWidgets.QPushButton(self.frame_4)
        self.bt_salvar.setMaximumSize(QtCore.QSize(110, 50))
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
        self.gridLayout_2.addWidget(self.bt_salvar, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_propri = QtWidgets.QPushButton(self.frame_5)
        self.bt_propri.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_propri.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";\n"
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
        self.bt_propri.setObjectName("bt_propri")
        self.horizontalLayout_2.addWidget(self.bt_propri)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela do Administrador"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ADMINISTRADOR</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Nome ADM:</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Login ADM:"))
        self.label_4.setText(_translate("MainWindow", "Senha ADM:"))
        self.label_5.setText(_translate("MainWindow", "EMPRESA:"))
        self.bt_salvar.setText(_translate("MainWindow", "SALVAR"))
        self.bt_propri.setText(_translate("MainWindow", "Propriedades"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Adm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()