class LeeJY:
    def __init__(self):
        self.money = 10
    def shout(self, angry):
        self.money += angry
    

class KimJU:
    def __init__(self):
        self.cnt_nuclear = 10
    def aoji(self):
        self.cnt_nuclear += 1
    

class LeeUC(LeeJY, KimJU):
    def __init__(self):
        LeeJY.__init__(self)
        KimJU.__init__(self)
    


    
lee = LeeUC()
print("LeeUC", lee.money)
print("LeeUC", lee.cnt_nuclear)

  
lee.shout(10)
lee.aoji()

print("LeeUC", lee.money)
print("LeeUC", lee.cnt_nuclear)
        
        
        