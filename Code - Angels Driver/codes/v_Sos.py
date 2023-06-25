from PyQt5 import QtCore, QtWidgets

class Ui_Sos(object):
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
        self.frame.setStyleSheet("background-color: rgb(136, 136, 136);")
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: white")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.bt_prf = QtWidgets.QPushButton(self.frame_3)
        self.bt_prf.setMaximumSize(QtCore.QSize(150, 70))
        self.bt_prf.setStyleSheet("QPushButton{background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 0);\n"
"font: 75 24pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: yellow;\n"
"border-radius: 10px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 0);\n"
"    color: rgb(0, 0, 0);\n"
"    border-color: black\n"
"}")
        self.bt_prf.setObjectName("bt_prf")
        self.gridLayout.addWidget(self.bt_prf, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.bt_pmr = QtWidgets.QPushButton(self.frame_4)
        self.bt_pmr.setMaximumSize(QtCore.QSize(150, 70))
        self.bt_pmr.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 127);\n"
"font: 75 24pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: blue;\n"
"border-radius: 10px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 127);\n"
"    color: rgb(255, 255, 255);\n"
"    border-color: white\n"
"}")
        self.bt_pmr.setObjectName("bt_pmr")
        self.gridLayout_2.addWidget(self.bt_pmr, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bt_pm = QtWidgets.QPushButton(self.frame_5)
        self.bt_pm.setMaximumSize(QtCore.QSize(150, 70))
        self.bt_pm.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 0, 127);\n"
"    color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Arial\";\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: white;\n"
"border-radius: 10px\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 127);\n"
"    border-color: blue\n"
"}")
        self.bt_pm.setObjectName("bt_pm")
        self.gridLayout_3.addWidget(self.bt_pm, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de SOS"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ACIONAR SOCORRO</p></body></html>"))
        self.bt_prf.setText(_translate("MainWindow", "PRF"))
        self.bt_pmr.setText(_translate("MainWindow", "PMR"))
        self.bt_pm.setText(_translate("MainWindow", "PM"))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Sos()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()