import sys


from PyQt5.QtWidgets import*
from PyQt5 import uic

FROM_CLASS_MainWindow = uic.loadUiType("myqt03.ui")[0]

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
        if (self.le1.text() == "") or (self.le2.text() == ""):
            QMessageBox.about(self, '경고','값이 없습니다.')
        else:
            a = int(self.le1.text())
            b =int(self.le2.text())
            self.le3.setText( str(a+b) )
      
        

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_() 
    
    




