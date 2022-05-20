import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QSize, QPushButton, QMessageBox
from envs.pythonProject.Lib.idlelib import tooltip
from _ast import Return
from boto import exception


FROM_CLASS = uic.loadUiType("myomok03_19.ui")[0]

class MainWindow(QMainWindow, FROM_CLASS):    

    
        
    def __init__(self):
    
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb2d=[]
        self.flag_wb = True;
        self.game = True;
        self.arr2d=[
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0]
        ]
        if self.game: 
            for i in range(19):  
                line = []
                for j in range(19):  
                    btn1 = QPushButton(self)
                    btn1.setText('')
                    btn1.setIcon(QtGui.QIcon('0.png'))
                    btn1.setIconSize(QSize(40, 40))
                    btn1.setGeometry(40*j,40*i,40,40)
                    btn1.clicked.connect(self.myclick)
                    btn1.setToolTip("{},{}".format(i,j))
                    line.append(btn1)
                self.pb2d.append(line)
                    
                    
                   
            self.myrender()
            #self.btn.clicked.connect(self.myclick)
            self.btn2.clicked.connect(self.reset)
            self.show()
        
    def myrender(self):
        for i in range(19):  
            for j in range(19):   
                if self.arr2d[i][j] == 0:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QtGui.QIcon('2.png'))
        
    
    def myclick(self):
        if self.game == False:
            return
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] > 0:
            return 
        
        stone = -1
        if self.flag_wb:
            self.arr2d[i][j] = 1
            stone = 1
        else:
            self.arr2d[i][j] = 2
            stone = 2
            
        up = self.checkUP(i,j,stone)
        dw = self.checkDW(i,j,stone)
        ri = self.checkRI(i,j,stone)
        le = self.checkLE(i,j,stone)
        leup = self.checkLEUP(i,j,stone)
        ridw = self.checkRIDW(i,j,stone)
        riup = self.checkRIUP(i,j,stone)
        ledw = self.checkLEDW(i,j,stone)
        print(up, dw, ri, le, leup, ridw, riup, ledw)
        a1 = up+dw
        a2 = ri+le
        a3 = leup+ridw
        a4 = riup+ledw
        
        
        self.myrender()    
        self.flag_wb = not self.flag_wb
        
        if a1 == 4 or a2 == 4 or a3 == 4 or a4 == 4:
            if stone == 1:
                QMessageBox.about(self, '축하합니다' , '흰돌이 이겼습니다' )
            if stone == 2:
                QMessageBox.about(self, '축하합니다' , '검은돌이 이겼습니다' )
            self.game = False;
            
            
        
    def checkUP(self,i,j,stone):
        cnt = 0;
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt   
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    
    def checkDW(self,i,j,stone):
        cnt = 0; 
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt       
        except:
            return cnt
        
        
        
    def checkRI(self,i,j,stone):
        cnt = 0;  
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt       
        except:
            return cnt
        
    
    def checkLE(self,i,j,stone):
        cnt = 0;  
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt       
        except:
            return cnt
        
    
    ## 왼쪽대각선    
        
    def checkLEUP(self,i,j,stone):
        cnt = 0;  
        try:
            while True:
                j -= 1
                i -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt       
        except:
            return cnt
        


    def checkRIDW(self,i,j,stone):
        cnt = 0;  
        try:
            while True:
                j += 1
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt       
        except:
            return cnt
    
    
    ## 오른쪽대각선
    
    def checkRIUP(self,i,j,stone):
        cnt = 0;  
        try:
            while True:
                j += 1
                i -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt       
        except:
            return cnt
        
    def checkLEDW(self,i,j,stone):
        cnt = 0;  
        try:
            while True:
                j -= 1
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2d[i][j] == stone:
                    cnt += 1
                else:
                    return cnt       
        except:
            return cnt
     
    
       
        
    
    def reset(self):
        for i in range(19):  
            for j in range(19):   
                self.pb2d[i][j].setIcon(QtGui.QIcon('0.png'))
                self.arr2d[i][j] = 0;
        self.game = True;
        #self.myrender()
 
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
    
    




