# a = input("좋아하는 수를 입력하세요")
# print(a)
import random
com=""
mine = input("홀짝을 입력하세요")
result = ""

ran = random.random()

if  ran > 0.5:
    com ="홀"
else:
    com ="짝"

if  com == mine:
    result ="이김"
else:
    result ="짐"

print("com:{}".format(com))
print("mine:{}".format(mine))
print("result:{}".format(result))