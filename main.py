from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import random
import time
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loadMainMenu()
    
    def loadMainMenu(self):
        uic.loadUi(r"F:\Projetos\Python\PicKei\Assets\qtGUI.ui", self)
        self.setWindowTitle("PicKei: O banco para você (Se você for o Kei)")
        
        self.QL_Dinheiro = self.findChild(QLabel, 'QL_Dinheiro')
        self.QL_Dinheiro.setText("R$0")
        self.QF_LogoTop = self.findChild(QFrame, 'QF_LogoTop')
        self.setLogoTop()
        
        self.DinheiroAtual = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.receberPix)
        
        #Recebe um pix a cada 15 segundos
        self.timer.start(15000)
       
        

    def receberPix(self):
        valuePix = random.randint(15, 634)    
        self.DinheiroAtual += valuePix
        self.QL_Dinheiro.setText(f"R${str(self.DinheiroAtual)},00")

        
    def setLogoTop(self):
        #QLabel em cima do QFrame setado as dimensões (LogoTop)
        pixmap = QPixmap('F:\Projetos\Python\PicKei\Assets\Logo.png')
        label = QLabel(self.QF_LogoTop)
        label.setPixmap(pixmap)
        label.setGeometry(5, 0, self.QF_LogoTop.width() - 25, self.QF_LogoTop.height())
        print("Dimensões QF_LogoTop: ", self.QF_LogoTop.width() - 25, self.QF_LogoTop.height())
        label.setScaledContents(True) 
    
    def setLogoPix(self):
        print("AAAAAAAAAAAAAAAAAAAAAAAA VAI SE FUDEEEE")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
