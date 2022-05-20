import sys


from PyQt5.QtWidgets import*
from PyQt5 import uic

FROM_CLASS_MainWindow = uic.loadUiType("myqt01.ui")[0]

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
        self.lbl.setText("Goog evening!!")
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_() 
    
    




