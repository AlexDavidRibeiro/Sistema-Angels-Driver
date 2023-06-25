from PyQt5 import QtCore, QtGui, QtWidgets
import logoAngels

class Ui_Login(object):
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
        self.frame_2.setStyleSheet("image: url(:/img/Angels driver.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("border-style: outset;\n"
"border-width: 1px;\n"
"border-color: black;\n"
"border-radius: 5px")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setStyleSheet("border-width: 0")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.ln_login = QtWidgets.QLineEdit(self.frame_4)
        self.ln_login.setMaximumSize(QtCore.QSize(240, 30))
        self.ln_login.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_login.setObjectName("ln_login")
        self.horizontalLayout_2.addWidget(self.ln_login)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setStyleSheet("border-width: 0")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setMaximumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.ln_senha = QtWidgets.QLineEdit(self.frame_5)
        self.ln_senha.setMaximumSize(QtCore.QSize(240, 30))
        self.ln_senha.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 12pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-radius: 5px;\n"
"padding-left: 5px")
        self.ln_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ln_senha.setObjectName("ln_senha")
        self.horizontalLayout_3.addWidget(self.ln_senha)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_6.setStyleSheet("border-width: 0")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.bt_entrar = QtWidgets.QPushButton(self.frame_6)
        self.bt_entrar.setMaximumSize(QtCore.QSize(110, 50))
        self.bt_entrar.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 127);\n"
"font: 75 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: white;\n"
"border-radius: 10px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 127);\n"
"    border-width: 2px;\n"
"    border-color: blue\n"
"\n"
"}")
        self.bt_entrar.setObjectName("bt_entrar")
        self.gridLayout.addWidget(self.bt_entrar, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela Angels Driver"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">LOGIN :</p></body></html>"))
        self.ln_login.setPlaceholderText(_translate("MainWindow", "Digite seu login..."))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">SENHA :</p></body></html>"))
        self.ln_senha.setPlaceholderText(_translate("MainWindow", "Digite sua senha..."))
        self.bt_entrar.setText(_translate("MainWindow", "ENTRAR"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    login = Ui_Login()
    login.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
