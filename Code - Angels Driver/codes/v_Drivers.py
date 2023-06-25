from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Driver(object):
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
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.frame.setFont(font)
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
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 360))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabela_listar = QtWidgets.QTableWidget(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabela_listar.setFont(font)
        self.tabela_listar.setStyleSheet("background-color: rgba(0, 0, 0, 0.3);\n"
"font: 75 10pt \"Arial\"")
        self.tabela_listar.setObjectName("tabela_listar")
        self.tabela_listar.setColumnCount(3)
        self.tabela_listar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_listar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_listar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_listar.setHorizontalHeaderItem(2, item)
        self.tabela_listar.horizontalHeader().setDefaultSectionSize(108)
        self.horizontalLayout_3.addWidget(self.tabela_listar)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_alterar = QtWidgets.QPushButton(self.frame_4)
        self.bt_alterar.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_alterar.setStyleSheet("QPushButton{\n"
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
        self.bt_alterar.setObjectName("bt_alterar")
        self.horizontalLayout_2.addWidget(self.bt_alterar)
        self.bt_excluir = QtWidgets.QPushButton(self.frame_4)
        self.bt_excluir.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_excluir.setStyleSheet("QPushButton{\n"
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
        self.bt_excluir.setObjectName("bt_excluir")
        self.horizontalLayout_2.addWidget(self.bt_excluir)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela Lista Driver"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">LISTA DRIVER</p></body></html>"))
        item = self.tabela_listar.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NOME"))
        item = self.tabela_listar.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.tabela_listar.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "LOGIN"))
        self.bt_alterar.setText(_translate("MainWindow", "ALTERAR"))
        self.bt_excluir.setText(_translate("MainWindow", "EXCLUIR"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Driver()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
