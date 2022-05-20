import sys


from PyQt5.QtWidgets import*
from PyQt5 import uic
import random

FROM_CLASS_MainWindow = uic.loadUiType("myqt04.ui")[0]

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
        ran = random.random();
        
        if ran >= 0.5:
            self.le_com.setText("홀")
        else:
            self.le_com.setText("짝")
            
        if ( self.le_mine.text() == self.le_com.text() ):
            result = "당신이 이겼습니다."
        else:
            result = "당신이 졌습니다."


        self.le_result.setText(result);
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_() 
    
    




