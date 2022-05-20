import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QSize, QPushButton


FROM_CLASS = uic.loadUiType("myomok01.ui")[0]

class MainWindow(QMainWindow, FROM_CLASS):    

    
        
    def __init__(self):
    
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.flag_wb = True
     
        for i in range(10):  
            for j in range(10):  
                btn1 = QPushButton(self)
                btn1.setText('')
                btn1.setIcon(QtGui.QIcon('0.png'))
                btn1.setIconSize(QSize(40, 40))
                btn1.setGeometry(40*j,40*i,40,40)
                btn1.clicked.connect(self.myclick)
                
                
        
        #self.btn.clicked.connect(self.myclick)
        self.btn2.clicked.connect(self.myclick2)
        self.show()
        
    
    def myclick(self):
        if self.flag_wb:
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else:
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flag_wb = not self.flag_wb
    
    
    def myclick2(self):
        print("myclick2")
 
 
 
    #def initUI(self):
        # for i in range(10):
        #     for j in range(10):
        #         #라벨 생성
        #         self.lbl = QLabel(self)
        #         self.lbl.resize(40, 40)
        #         self.lbl.move(40*i,40*j)
        #
        #
        #         #이미지 관련 클래스 생성 및 이미지 불러오기 
        #         pixmap = QPixmap('0.png')
        #
        #
        #         #이미지 관련 클래스와 라벨 연결 
        #         self.lbl.setPixmap(QPixmap(pixmap))
        # #self.resize(pixmap.width()+20,pixmap.height()+20)
        # self.resize(500, 500)
        # self.show()
    #  self.pb_1.setStyleSheet('border-image:url(./0.png)')
  
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_() 
    
    




