# 1~9까지의 수 중에서 3가지를 랜덤 중복없이 출력하시오
import random;


########## 방법1 #########
# ran = random.randint(1,9);
# a = ran;
# ran1 = random.randint(1,9);
# b = ran1;
# ran2 = random.randint(1,9);
# c = ran2;
#
# while b == a:
#    ran1 = random.randint(1,9);
#    b = ran1
#
# while c == a or c == b:
#    ran2 = random.randint(1,9);
#    c = ran2
#
#
# print(a,b,c)







########## 방법2 #########

# arr9 = [1,2,3,4,5,6,7,8,9]
#
# for i in range(100):
#     rnd = int(random.random()*9)
#     temp = arr9[rnd]
#     arr9[rnd] = arr9[1]
#     arr9[1] = temp
#
#
# #print(arr9[0],arr9[1],arr9[2])
# # 배열자르기
# print(arr9[0:3])




########## 방법3 #########

arr45 = list(range(1,45+1))
arr6 = []

while True:
    rnd = int(random.random()*45)
    if arr45[rnd] == -1:
        pass
    else:
        arr6.append(arr45[rnd])
        arr45[rnd] = -1
    if len(arr6) >= 6:
        break
print(arr6)










