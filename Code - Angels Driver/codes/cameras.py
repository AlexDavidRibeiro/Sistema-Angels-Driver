from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import Qt
import cv2

from v_Cameras import Ui_Cameras

class Cameras:
    def __init__(self) -> None:
        self.MainWindow = QtWidgets.QMainWindow()
        self.cam = Ui_Cameras()
        self.cam.setupUi(self.MainWindow)
        #self.cam.bt_tempo.clicked.connect()
        self.cam.bt_voltar.clicked.connect(self.stopCams)
        self.cameraTraseira()
        #self.cameraDianteira() # Ativar quando houver uma segunda câmera
    
    def cameraTraseira(self):  # Função OK  
        self.MainWindow.show()
        
        cap = cv2.VideoCapture(0) # Valor 0 representa a primeira câmera (Traseira)
        
        global Atividade
        Atividade = True

        while Atividade:

            ret, frame = cap.read()
                
            if ret == False: break

            imagem = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            flip = cv2.flip(imagem,1)
            ConvertQT = QImage(flip.data, flip.shape[1],flip.shape[0],QImage.Format_RGB888)
            picture = ConvertQT.scaled(400, 305,Qt.KeepAspectRatio)
            self.cam.lb_camT.setPixmap(QPixmap.fromImage(picture))

            cv2.waitKey()
                  
        cap.release()
        cv2.destroyAllWindows()

    def cameraDianteira(self):  # Função OK   
        self.MainWindow.show()

        cap = cv2.VideoCapture(1) # Valor 1 representa a segunda câmera(Dianteira) 

        global Atividade
        Atividade = True

        while Atividade:

            ret, frame = cap.read()
                
            if ret == False: break

            imagem = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            flip = cv2.flip(imagem,1)
            ConvertQT = QImage(flip.data, flip.shape[1],flip.shape[0],QImage.Format_RGB888)
            picture = ConvertQT.scaled(400, 305,Qt.KeepAspectRatio)
            self.cam.lb_camD.setPixmap(QPixmap.fromImage(picture))

            cv2.waitKey()
                  
        cap.release()
        cv2.destroyAllWindows()

    def stopCams(self):  # Função OK
        global Atividade
        Atividade = False
        self.MainWindow.close()
        print("Desativando a visualização das câmeras")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    sistema = Cameras()
    app.exec()