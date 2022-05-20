#가위 바위 보를 선택 하세요. 가위 Enter
#나: 가위
#컴: 바위
# 결과: 짐
import random

me = input("가위,바위,보를 선택하세요")
ran = random.random()
com = ""
print0=""

if ran>=0.7:
    com = "가위"
elif ran>=0.3:
    com = "바위"
else:
    com = "보"

if com == "가위" and me == "바위" or com == "바위" and me == "보" or com == "보" and me == "가위":
    print0 = "결과: 당신이 이겼습니다."
elif com ==  me:
    print0 = "결과: 비겼습니다."
else:
    print0 = "결과: 당신이 졌습니다."

print("나:{}".format(me))
print("컴:{}".format(com))
print(print0)