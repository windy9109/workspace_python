import sys


from PyQt5.QtWidgets import*
from PyQt5 import uic
import random
from _ast import Or

FROM_CLASS_MainWindow = uic.loadUiType("myqt09.ui")[0]

class MainWindow(QMainWindow,FROM_CLASS_MainWindow):    

    def __init__(self):
        super().__init__()
        
        # UI 파일 로드
        self.setupUi(self) 
        self.show()
        
        
        # 버튼 클릭 매서드
        self.btn.clicked.connect(self.button0)
        self.leMine.returnPressed.connect(self.button0)
    
      
        
    def button0(self):
        #QMessageBox.about(self, '눌림알람','눌렀삼')  
        ran = random.random();
        
        if ran >= 0.66:
            self.leCom.setText("가위")
        elif ran >= 0.33:
            self.leCom.setText("바위")
        else: 
            self.leCom.setText("보")
        
        Mine = self.leMine.text()
        Com = self.leCom.text()  
        
        if ( Mine == Com ):
            result = "비겼습니다."
        elif ( Mine == "가위" and Com  == "보") or ( Mine == "바위" and Com  == "가위") or ( Mine == "보" and Com  == "바위"):
            result = "당신이 이겼습니다."
        else:
            result = "당신이 졌습니다."

        self.leResult.setText(result);
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_() 
    
    




