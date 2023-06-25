from PyQt5 import QtCore, QtWidgets

class Ui_Alerta(object):
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
        self.frame.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(100, 80))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMaximumSize(QtCore.QSize(70, 35))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(70, 35))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_socorro = QtWidgets.QPushButton(self.frame_6)
        self.bt_socorro.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_socorro.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: white\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 0, 0);\n"
"    border-color: red\n"
"}")
        self.bt_socorro.setObjectName("bt_socorro")
        self.horizontalLayout_2.addWidget(self.bt_socorro)
        self.bt_vigiar = QtWidgets.QPushButton(self.frame_6)
        self.bt_vigiar.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_vigiar.setStyleSheet("QPushButton{\n"
"background-color: rgb(220, 220, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: white\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(230, 230, 0);\n"
"    border-color: yellow\n"
"}")
        self.bt_vigiar.setObjectName("bt_vigiar")
        self.horizontalLayout_2.addWidget(self.bt_vigiar)
        self.bt_cancelar = QtWidgets.QPushButton(self.frame_6)
        self.bt_cancelar.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_cancelar.setStyleSheet("QPushButton{\n"
"background-color: rgb(65, 195, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: white\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(65, 195, 0);\n"
"    border-color: green\n"
"}")
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.horizontalLayout_2.addWidget(self.bt_cancelar)
        self.gridLayout.addWidget(self.frame_6, 3, 0, 1, 2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ln_placa = QtWidgets.QLineEdit(self.frame_4)
        self.ln_placa.setMaximumSize(QtCore.QSize(150, 30))
        self.ln_placa.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 75 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"border-color: white")
        self.ln_placa.setText("")
        self.ln_placa.setObjectName("ln_placa")
        self.verticalLayout_2.addWidget(self.ln_placa)
        self.ln_tempo = QtWidgets.QLineEdit(self.frame_4)
        self.ln_tempo.setMaximumSize(QtCore.QSize(100, 30))
        self.ln_tempo.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 75 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"border-color: white")
        self.ln_tempo.setText("")
        self.ln_tempo.setObjectName("ln_tempo")
        self.verticalLayout_2.addWidget(self.ln_tempo)
        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(270, 35))
        self.label.setStyleSheet("font: 75 16pt \"Arial\";\n"
"color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_foto = QtWidgets.QLabel(self.frame_5)
        self.lb_foto.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-color: white")
        self.lb_foto.setObjectName("lb_foto")
        self.horizontalLayout_3.addWidget(self.lb_foto)
        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de Alerta"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">PLACA :</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">TEMPO :</p></body></html>"))
        self.bt_socorro.setText(_translate("MainWindow", "Socorro"))
        self.bt_vigiar.setText(_translate("MainWindow", "Vigiar"))
        self.bt_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ALERTA - Atividade Suspeita</p></body></html>"))
        self.lb_foto.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Foto do veículo suspeito</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Alerta()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
