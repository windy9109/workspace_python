# 1~45까지의 수 중에서 6가지를 랜덤 중복없이 출력하시오 로또프로그램
import random


a = []
for i in range(1,45+1):
    a.append(i)



random.shuffle(a)


for i in range(0,6):
    print(a[i])



# for i in a:
#     b.append(random.randint(0,6))
#     #str = b[i]
#     for j in range(0,i+1):
#         while b[i] == b[j] and i != j:
#             b[i] = random.randint(0,6)
#             --j;
#
#         print("b[{}]내용:{}, b[{}]내용:{}".format( i, b[i], j, b[j]))
#     print("--------------------")
       



