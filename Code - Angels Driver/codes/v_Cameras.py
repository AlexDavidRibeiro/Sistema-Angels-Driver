from PyQt5 import QtCore, QtWidgets

class Ui_Cameras(object):
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
        self.frame.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_tempo = QtWidgets.QPushButton(self.frame_2)
        self.bt_tempo.setMaximumSize(QtCore.QSize(90, 30))
        self.bt_tempo.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 170, 0);\n"
"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width: 2px;\n"
"border-color: white\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 170, 0);\n"
"    border-width: 2px;\n"
"    border-color: rgb(0, 170, 0)\n"
"}")
        self.bt_tempo.setObjectName("bt_tempo")
        self.horizontalLayout_4.addWidget(self.bt_tempo)
        self.bt_voltar = QtWidgets.QPushButton(self.frame_2)
        self.bt_voltar.setMaximumSize(QtCore.QSize(90, 30))
        self.bt_voltar.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"border-width: 2px;\n"
"border-color: white\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 0, 0);\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 0, 0)\n"
"}")
        self.bt_voltar.setObjectName("bt_tempo_2")
        self.horizontalLayout_4.addWidget(self.bt_voltar)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_camT = QtWidgets.QLabel(self.frame_3)
        self.lb_camT.setMaximumSize(QtCore.QSize(340, 205))
        self.lb_camT.setObjectName("lb_camT")
        self.horizontalLayout_2.addWidget(self.lb_camT)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_camD = QtWidgets.QLabel(self.frame_4)
        self.lb_camD.setMaximumSize(QtCore.QSize(340, 205))
        self.lb_camD.setObjectName("lb_camD")
        self.horizontalLayout_3.addWidget(self.lb_camD)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela das Câmeras"))
        self.bt_tempo.setText(_translate("MainWindow", "Tempo"))
        self.bt_voltar.setText(_translate("MainWindow", "Voltar"))
        self.lb_camT.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lb_camD.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Cameras()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()