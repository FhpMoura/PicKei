from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QVBoxLayout, QApplication, QFrame, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import os
import subprocess
import random
import sys

CharactersList = {
    "Edward Elric": ["Amo shibas eles são tão friend shaped", r".\Assets\chars\edward.png"],
    "Ren Kano": ["Em Bayonetta 2 o Luka virou uma passiva toxica", r".\Assets\chars\ren.png"],
    "Imbibitor Lunae": ["Um twink, um idoso, um viado e um evangelion", r".\Assets\chars\imbi.png"],
    "Zhongli": ["nossa que vontade de dar de maluco forjar meu suicidio de novo e sumir", r".\Assets\chars\zhon.png"],
    "Baji Keisue": ["Se um moleque aleatorio chamou a atenção da Bayonetta porquê eu nao conseguiria", r".\Assets\chars\baji.png"],
    "Noctis Lucis": ["Olá amigos da falecida rodinha", r".\Assets\chars\noctis.png"],
    "Cloud Strife": ["silly", r".\Assets\chars\cloud.png"],
    "Naoto Shirogane": ["JFIOW$EJFSDKLfjdskl", r".\Assets\chars\naoto.png"],
    "Ichika Hoshino": ["i play the guitar", r".\Assets\chars\ichika.png"],
    "Luna": ["Oi você esqueceu de me bloquear no PicKei", r".\Assets\chars\luna.png"],
    "Mello": ["SEUS PUTOS PAREM DE TROCAR DE USER - mello", r".\Assets\chars\mello.png"],
    "Luke": ["Mandar Pix, Me manda de volta", r".\Assets\chars\luke.png"],
    "Caetano": ["neymar é madarap e kanatap", r".\Assets\chars\caeta.png"],
    "Rod": ["I got daddy issues that's so me!", r".\Assets\chars\rod.png"],
    "Gabi": ["Top builds, runes, skill orders for Yasuo", r".\Assets\chars\gabi.png"],
    "Mio": ["Meu pix é isso aqui 🙏🙏", r".\Assets\chars\mio.png"]
}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loadMainMenu()
    
    def loadMainMenu(self):
        uic.loadUi(r".\Assets\qtGUI.ui", self)
        self.setWindowTitle("PicKei: O banco para você (Se você for o Kei)")
        
        self.QL_Dinheiro = self.findChild(QLabel, 'QL_Dinheiro')
        self.QL_Nome = self.findChild(QLabel, 'QL_Nome')
        self.QL_Valor = self.findChild(QLabel, 'QL_Valor')
        self.QL_Descricao = self.findChild(QLabel, 'QL_Descricao')
        self.QF_LogoTop = self.findChild(QFrame, 'QF_LogoTop')
        self.QL_SenderPix = self.findChild(QLabel, 'QL_SenderPix')
        self.QPB_Deposito = self.findChild(QPushButton, 'QPB_Deposito')
        self.QPB_EnviarPix = self.findChild(QPushButton, 'QPB_EnviarPix')

        self.QL_Dinheiro.setText("R$0")
        self.setLogoTop()
        self.DinheiroAtual = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.receberPix)
        self.QPB_Deposito.clicked.connect(self.abrirKeilinho)
        self.QPB_EnviarPix.clicked.connect(self.enviarPix)
        #Recebe um pix a cada 15 segundos
        self.timer.start(7000)
        

    def receberPix(self):
        valuePix = random.randint(15, 634)    
        self.DinheiroAtual += valuePix
        self.QL_Dinheiro.setText(f"R${str(self.DinheiroAtual)},00")

        self.SenderPix = random.choice(list(CharactersList.keys()))
        self.QL_Nome.setText(f"Nome: {self.SenderPix}")
        self.QL_Valor.setText(f"Valor: R${valuePix},00")
        self.QL_Descricao.setText(f"Descrição: {CharactersList[self.SenderPix][0]}")

        pixmap = QPixmap(CharactersList[self.SenderPix][1])
        label = QLabel(self.QL_SenderPix)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, self.QL_SenderPix.width(), self.QL_SenderPix.height())
        label.setScaledContents(True) 
        label.show()

    def abrirKeilinho(self):
        os.startfile('deposito.png')

    def setLogoTop(self):
        #QLabel em cima do QFrame setado as dimensões (LogoTop)
        pixmap = QPixmap(r'.\Assets\Logo.png')
        label = QLabel(self.QF_LogoTop)
        label.setPixmap(pixmap)
        label.setGeometry(5, 0, self.QF_LogoTop.width() - 25, self.QF_LogoTop.height())
        print("Dimensões QF_LogoTop: ", self.QF_LogoTop.width() - 25, self.QF_LogoTop.height())
        label.setScaledContents(True) 
    
    def enviarPix(self):
        result = subprocess.run(['cscript.exe', r'.\Inspec\script.vbs'], capture_output=True, text=True)
        output = result.stdout.splitlines()

        self.dinheiroEnviado = int(output[4])
        self.DinheiroAtual -= self.dinheiroEnviado

        print(result)
        print(output)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
