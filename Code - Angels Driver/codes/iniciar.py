from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PIL import Image
import pytesseract
import sqlite3
import cv2
import os
import pyautogui as py

from v_Iniciar import Ui_Iniciar
from alerta import Alerta
from cadDriver import Config
from cameras import Cameras

class Iniciar:
    def __init__(self) -> None:
        global adm
        self.MainWindow = QtWidgets.QMainWindow()
        self.start = Ui_Iniciar()
        self.start.setupUi(self.MainWindow)
        if adm == 0:
            self.start.bt_ADM.clicked.connect(self.config)
        self.start.bt_alerta.clicked.connect(self.alerta)
        self.start.bt_cameras.clicked.connect(self.cameras)
        self.start.bt_iniciar.clicked.connect(self.inicio)
        self.start.bt_encerrar.clicked.connect(self.encerrar)
        self.MainWindow.show()

    def startup(x): # Função OK
        global adm
        adm = x
            
    def config(self): # Função OK
        print("Acesso às configurações do administrador")
        self.sistema = Config()

    def inicio(self):

        def reconhecimento():
            ocr = cv2.imread(r'placas\ocr.png')
                                   
            if ocr is None: return
                    
            config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            saida = pytesseract.image_to_string(ocr, lang='eng', config=config)
                  
            img = Image.open("placas/FotoPlaca.png").convert("RGB")
            lar = img.width//2                    # Configurando a largura da imagem em 50%
            alt = img.height//2                   # Configurando a altura da imagem em 50%
            img_resize = img.resize((lar,alt))    # Organizando a imagem
            img_resize.save("fotos/placa.jpg")    # Salvando a imagem configurada
                    
            if 7 <= len(saida) < 9:
                con = sqlite3.connect('database\AngelsDriver.db')

                tempo = 2             # Intervalo, em segundos, de captura das câmeras 
                b = [saida,tempo]     # Placa e tempo para adicionar no BD
                time=0                # Para cada placa repetida, soma-se mais 2 segundos  de tempo

                with con:
                    seta = con.cursor()
                    sql = "SELECT * FROM Placas"
                    seta.execute(sql)
                    dados = seta.fetchall()

                    if dados == []:
                        sql = "INSERT INTO Placas (Placas, tempo) VALUES (?,?)"
                        seta.execute(sql, b)
                        #Iniciar.regPlacaTras()        
                    else:
                        sql = "INSERT INTO Placas (Placas, tempo) VALUES (?,?)"
                        seta.execute(sql,b)
                        print("Valores inseridos com sucesso")
                        #Iniciar.regPlacaDia() 

                    for i in range(0,len(dados)):
                        if dados[i][1] == saida:
                            time = dados[i][2]+2
                            fim = [time,saida]
                            sql="UPDATE Placas SET Tempo=? WHERE Placas=?"
                            seta.execute(sql,fim)
                            sql="DELETE FROM Placas WHERE Id_Placa=?"
                            data= [dados[i][0]]
                            seta.execute(sql,data)
                            print("ATUALIZADO")

            #Alert.exibeDados()  # Envia dados para serem processados   

            # Os códigos abaixo, excluem as fotos antigas da pasta placas
                   
            excluir = r'placas'

            for root, dirs, files in os.walk(excluir):
                for file in files:
                    eliminar = os.path.join(root,file)
                    if '.png' in file:
                        os.remove(eliminar)

        def processamento():
            plate = cv2.imread(r'placas\placa.png')
                                       
            if plate is None: return

            img = cv2.resize(plate, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC) # redimensiona a placa em 2x
            img = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY) # Converte para escala de cinza
            _, img = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY) # Binariza imagem em preto e branco
            img = cv2.GaussianBlur(img, (5, 5), 0) # Desfoque na Imagem
                                        
            cv2.imwrite(r'placas\ocr.png', img) # Aplica reconhecimento OCR no ROI com o Tesseract
                                    
            reconhecimento()

        def drawContornos(contorno,area):
            for c in contorno:
                perimetro = cv2.arcLength(c, True) # perimetro do contorno, verifica se o contorno é fechado

                if perimetro > 300:
                    aprox = cv2.approxPolyDP(c, 0.08 * perimetro, True) # aproxima os contornos da forma correspondente
                                        
                    if len(aprox) == 4:  # verifica se é um quadrado ou retangulo de acordo com a qtd de vertices
                        (x, y, alt, lar) = cv2.boundingRect(c) # Contorna a placa atraves dos contornos encontrados
                        cv2.rectangle(area, (x, y), (x + alt, y + lar), (0, 255, 0), 2)
                        placa = area[y:y + lar, x:x + alt]  # segmenta a placa da imagem
                        cv2.imwrite(r'placas\placa.png', placa) 

        origem = self.start.ln_origem.text()
        destino = self.start.ln_destino.text()
        local = [origem,destino]

        if origem != "" and destino != "":
            con = sqlite3.connect('database\AngelsDriver.db')  # Conectando com o Banco de Dados

            local = [origem,destino]

            with con:
                seta = con.cursor()
                sql = "INSERT INTO Iniciar (Origem, Destino) VALUES (?,?)"
                seta.execute(sql,local)
            
            global Capturar
            Capturar = True
            
            while Capturar:
                video = cv2.VideoCapture(0)

                n = 2
                while n != 0:
                    valida, frame = video.read()

                    if (valida == False): break
                                            
                    area = frame[300:,:640]  # area de localização de captura
                    cinza = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY) # escala de cinza
                    valida, cinza = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY) # limiarização, destaca itens 
                    cinza = cv2.GaussianBlur(cinza, (5, 5), 0) # desfoque
                    contorno, hier  = cv2.findContours(cinza, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # lista os contornos
                    cv2.imwrite(r'placas\FotoPlaca.png', frame)                
                                
                    drawContornos(contorno, area)

                    #cv2.imshow('',area) # Comando para exibir a imagem de teste
                    if cv2.waitKey(1) & 0xff == 27: break
                            
                    py.sleep(1)
                    py.press('esc')
                    n-=1
                                    
                video.release()
                processamento()
                cv2.destroyAllWindows()

                if n == 0:
                    py.sleep(1)
                    n = 2 

        else:
            QMessageBox.warning(QMessageBox(),"CAMPOS VAZIOS","Os campos ORIGEM ou DESTINO não podem estar vazios.")

    def encerrar(self): # Função OK
        print("Encerrando o sistema")
        global Capturar
        Capturar = False

    def regPlacaTras(self):
        con = sqlite3.connect('database\AngelsDriver.db')

        with con:
            seta = con.cursor()
            sql = "SELECT Placas, Tempo FROM Placas"
            seta.execute(sql)
            dados = seta.fetchall()

            self.start.tabela_tras.setRowCount(len(dados)) # Conta quantos elementos possui em cada linha
            self.start.tabela_tras.setColumnCount(2)       # Quantidade de colunas pré determinadas

            for i in range (0, len(dados)): # Loop que organiza os dados para exibição
                for j in range (0,2):
                    self.start.tabela_tras.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))

    def regPlacaDia(self):
        con = sqlite3.connect('database\AngelsDriver.db')

        with con:
            seta = con.cursor()
            sql = "SELECT Placas, Tempo FROM Placas"
            seta.execute(sql)
            dados = seta.fetchall()

            self.start.tabela_dia.setRowCount(len(dados)) # Conta quantos elementos possui em cada linha
            self.start.tabela_dia.setColumnCount(2)       # Quantidade de colunas pré determinadas

            for i in range (0, len(dados)): # Loop que organiza os dados para exibição
                for j in range (0,2):
                    self.start.tabela_dia.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))

    def maps(self):
        pass

    def alerta(self): # Função OK
        print("Alerta manual ativado")
        self.sistema = Alerta()

    def cameras(self): # Função OK
        print("Câmeras acionadas")
        self.sistema = Cameras()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    sistema = Iniciar()
    app.exec()