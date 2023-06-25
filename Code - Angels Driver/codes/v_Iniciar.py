from PyQt5 import QtCore, QtGui, QtWidgets
import icoAdmin

class Ui_Iniciar(object):
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
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setMaximumSize(QtCore.QSize(70, 30))
        self.label.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.ln_origem = QtWidgets.QLineEdit(self.frame_6)
        self.ln_origem.setMaximumSize(QtCore.QSize(255, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ln_origem.setFont(font)
        self.ln_origem.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 5px;\n"
"border-radius: 5px")
        self.ln_origem.setObjectName("ln_origem")
        self.horizontalLayout_3.addWidget(self.ln_origem)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setMaximumSize(QtCore.QSize(70, 30))
        self.label_2.setStyleSheet("font: 75 12pt \"Arial\";\n"
"color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ln_destino = QtWidgets.QLineEdit(self.frame_7)
        self.ln_destino.setMaximumSize(QtCore.QSize(255, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ln_destino.setFont(font)
        self.ln_destino.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 5px;\n"
"border-radius: 5px;")
        self.ln_destino.setObjectName("ln_destino")
        self.horizontalLayout_2.addWidget(self.ln_destino)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bt_ADM = QtWidgets.QToolButton(self.frame_3)
        self.bt_ADM.setMaximumSize(QtCore.QSize(50, 50))
        self.bt_ADM.setStyleSheet("QToolButton{\n"
"image: url(:/img/admin.png);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"QToolButton:pressed{\n"
"    \n"
"    background-color: rgb(0, 255, 255);\n"
"}")
        self.bt_ADM.setText("")
        self.bt_ADM.setObjectName("bt_ADM")
        self.horizontalLayout_6.addWidget(self.bt_ADM)
        self.bt_iniciar = QtWidgets.QToolButton(self.frame_3)
        self.bt_iniciar.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bt_iniciar.setFont(font)
        self.bt_iniciar.setStyleSheet("QToolButton{\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"QToolButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 170, 0);\n"
"    border-width: 2px\n"
"}")
        self.bt_iniciar.setObjectName("bt_iniciar")
        self.horizontalLayout_6.addWidget(self.bt_iniciar)
        self.bt_encerrar = QtWidgets.QToolButton(self.frame_3)
        self.bt_encerrar.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bt_encerrar.setFont(font)
        self.bt_encerrar.setStyleSheet("QToolButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"QToolButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 0, 0);\n"
"    border-width: 2px\n"
"}")
        self.bt_encerrar.setObjectName("bt_iniciar_2")
        self.horizontalLayout_6.addWidget(self.bt_encerrar)
        self.bt_maps = QtWidgets.QToolButton(self.frame_3)
        self.bt_maps.setMaximumSize(QtCore.QSize(50, 50))
        self.bt_maps.setStyleSheet("QToolButton{\n"
"image: url(:/img/maps.png);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"QToolButton:pressed{\n"
"    background-color: rgb(0, 255, 255);\n"
"}")
        self.bt_maps.setText("")
        self.bt_maps.setObjectName("bt_maps")
        self.horizontalLayout_6.addWidget(self.bt_maps)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 230))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabela_tras = QtWidgets.QTableWidget(self.frame_4)
        self.tabela_tras.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.tabela_tras.setObjectName("tabela_tras")
        self.tabela_tras.setColumnCount(1)
        self.tabela_tras.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tabela_tras.setHorizontalHeaderItem(0, item)
        self.tabela_tras.horizontalHeader().setDefaultSectionSize(170)
        self.horizontalLayout_5.addWidget(self.tabela_tras)
        self.tabela_dia = QtWidgets.QTableWidget(self.frame_4)
        self.tabela_dia.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.tabela_dia.setObjectName("tabela_dia")
        self.tabela_dia.setColumnCount(1)
        self.tabela_dia.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        item.setFont(font)
        self.tabela_dia.setHorizontalHeaderItem(0, item)
        self.tabela_dia.horizontalHeader().setDefaultSectionSize(170)
        self.horizontalLayout_5.addWidget(self.tabela_dia)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_alerta = QtWidgets.QToolButton(self.frame_5)
        self.bt_alerta.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_alerta.setFont(font)
        self.bt_alerta.setStyleSheet("QToolButton{\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"QToolButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(255, 0, 0);\n"
"    border-width: 2px\n"
"}")
        self.bt_alerta.setObjectName("bt_alerta")
        self.horizontalLayout_4.addWidget(self.bt_alerta)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.bt_cameras = QtWidgets.QToolButton(self.frame_5)
        self.bt_cameras.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_cameras.setFont(font)
        self.bt_cameras.setStyleSheet("QToolButton{\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"QToolButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 127);\n"
"    border-width: 2px\n"
"}")
        self.bt_cameras.setObjectName("bt_cameras")
        self.horizontalLayout_4.addWidget(self.bt_cameras)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela Iniciar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Origem :</p></body></html>"))
        self.ln_origem.setPlaceholderText(_translate("MainWindow", "Cidade de origem..."))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Destino :</p></body></html>"))
        self.ln_destino.setPlaceholderText(_translate("MainWindow", "Cidade de Destino..."))
        self.bt_iniciar.setText(_translate("MainWindow", "   INICIAR   "))
        self.bt_encerrar.setText(_translate("MainWindow", "ENCERRAR"))
        item = self.tabela_tras.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Placas Câmera Traseira"))
        item = self.tabela_dia.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Placas Câmera Diânteira"))
        self.bt_alerta.setText(_translate("MainWindow", "  ALERTA  "))
        self.bt_cameras.setText(_translate("MainWindow", "CÂMERAS"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Iniciar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()