import sys


from PyQt5.QtWidgets import*
from PyQt5 import uic
import random

FROM_CLASS_MainWindow = uic.loadUiType("myqt06.ui")[0]

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
        
        arr = list(range(1,45+1))

 
        
        for i in range(1000):
            ran = int(random.random()*45);
            temp = arr[ran];
            arr[ran] = arr[1];
            arr[1] = temp;
        
        
        self.lbl_1.setText(str(arr[1]))
        self.lbl_2.setText(str(arr[2]))  
        self.lbl_3.setText(str(arr[3]))
        self.lbl_4.setText(str(arr[4])) 
        self.lbl_5.setText(str(arr[5]))
        self.lbl_6.setText(str(arr[6])) 
        
        
        ############### 방법2 #################
        
        # arr = list(range(1,45+1))
        # arr6 = []
        #
        # while True:
        #     ran = int(random.random()*45)
        #     if arr[ran] == -1:
        #         pass
        #     else:
        #         arr6.append(arr[ran])
        #         arr[ran] = -1;
        #     if len(arr6) >= 6:
        #         break
        #
        #
        # self.lbl_1.setText(str(arr6[0]))
        # self.lbl_2.setText(str(arr6[1]))  
        # self.lbl_3.setText(str(arr6[2]))
        # self.lbl_4.setText(str(arr6[3])) 
        # self.lbl_5.setText(str(arr6[4]))
        # self.lbl_6.setText(str(arr6[5])) 
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_() 
    
    




