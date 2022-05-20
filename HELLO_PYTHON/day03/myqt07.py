import sys


from PyQt5.QtWidgets import*
from PyQt5 import uic

FROM_CLASS_MainWindow = uic.loadUiType("myqt07.ui")[0]

class MainWindow(QMainWindow,FROM_CLASS_MainWindow):    

    def __init__(self):
        super().__init__()
        
        # UI 파일 로드
        self.setupUi(self) 
        self.show()
        
        
        # 버튼 클릭 매서드
        self.btn.clicked.connect(self.button0)
        
        
    def button0(self):
        #QMessageBox.about(self, '눌림알람','눌렀삼')  
        # self.le_f.text()
        # self.le_l.text()
        a = ""
        for i in range(int(self.le_f.text()),int(self.le_l.text())+1):
            a += self.drawStar(i)
        
        self.te.setText(str(a));
    
    
    def drawStar(self,cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_() 
    
    




