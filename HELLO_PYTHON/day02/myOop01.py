
class Animal:
    
    
    def __init__(self):
        print("Animal:생성자")
        self.age = 0
        
    def getOld(self):
        self.age += 1
        
    
    def __del__ (self):
        print("Animal:소멸자")
        
if __name__ == '__main__':
        ani = Animal()
        print("myoop021",ani.age)
        
        ani.getOld()
        print("myoop021", ani.age)


ani = Animal()
print(ani.age)
ani.getOld()
print(ani.age)    
    



class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skill_lang = 1
        print("Human:생성자")
        
    def momstouch(self, stroke):
        self.skill_lang += stroke
        
    def __del__ (self):
         print("Human:소멸자")

if __name__ == '__main__':
        hum = Human()
        print("myoop03",hum.skill_lang)
        print("myoop03",hum.age)

        hum.getOld()
        hum.momstouch(100)
        print("myoop03", hum.skill_lang)
        print("myoop03", hum.age)

        


        
         
        
