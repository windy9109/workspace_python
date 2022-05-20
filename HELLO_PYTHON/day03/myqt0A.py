import sys


from PyQt5.QtWidgets import*
from PyQt5 import uic
import random

FROM_CLASS_MainWindow = uic.loadUiType("myqt0A.ui")[0]

class MainWindow(QMainWindow,FROM_CLASS_MainWindow):    

    def __init__(self):
        super().__init__()
        # UI 파일 로드
        self.setupUi(self) 
        self.show()
        self.a= (int)(random.random()*9);
        self.b= (int)(random.random()*9);
        self.c= (int)(random.random()*9);

    
        
        # 버튼 클릭 매서드
        self.random0()
        self.btn.clicked.connect(self.button0)
        self.le.returnPressed.connect(self.button0)
        
        
        
    def random0(self):   
        while self.a == self.b or self.a == self.c or self.b == self.c :
            self.a= (int)(random.random()*9);
            self.b= (int)(random.random()*9);
            self.c= (int)(random.random()*9);
        
        
    def button0(self):
        #QMessageBox.about(self, '눌림알람','눌렀삼')  

         
        s1=0;
        b1=0;
        
        
        num = int(self.le.text());
        

        num1 = (int)(num/100); 
        num2 = ((int)(num/10))%10; 
        num3 = num%10;
        
        number = [ num1,num2,num3 ]
        com = [ self.a,self.b,self.c ]
        
        for i in range(len(number)):
            for j in range(len(number)) :
                if( number[i] == com[j] and i == j):
                    s1 += 1
                if( number[i] == com[j] and i != j):
                    b1 += 1
        
        
        if(s1 == 3):
            QMessageBox.about(self, 'Calling', '모두 맞췄습니다! 축하합니다!')
        
        
        str_new = "컴:{},{},{} / 나:{} / s:{}, b{} \n".format(self.a,self.b,self.c,num,s1,b1);
        str_old = self.te.toPlainText();
        
        self.te.setPlainText(str(str_old)+str(str_new));
        self.le.setText("");
        
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_() 
    
    




