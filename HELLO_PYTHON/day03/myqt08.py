import sys


from PyQt5.QtWidgets import*
from PyQt5 import uic

FROM_CLASS_MainWindow = uic.loadUiType("myqt08.ui")[0]

class MainWindow(QMainWindow,FROM_CLASS_MainWindow):    

    def __init__(self):
        super().__init__()
        
        # UI 파일 로드
        self.setupUi(self) 
        self.show()
        
        
        # 버튼 클릭 매서드
        self.pb_1.clicked.connect(self.myclick)
        self.pb_2.clicked.connect(self.myclick)
        self.pb_3.clicked.connect(self.myclick)
        self.pb_4.clicked.connect(self.myclick)
        self.pb_5.clicked.connect(self.myclick)
        self.pb_6.clicked.connect(self.myclick)
        self.pb_7.clicked.connect(self.myclick)
        self.pb_8.clicked.connect(self.myclick)
        self.pb_9.clicked.connect(self.myclick)
        self.pb_0.clicked.connect(self.myclick)
        self.pb_call.clicked.connect(self.call)
        
        

    def myclick(self):
        oldText = self.le.text()
        newText = self.sender().text()
        self.le.setText(oldText+newText)
    
 
    
    def call(self):
        
        QMessageBox.about(self, 'call알람', self.le.text())
            
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_() 
    
    




