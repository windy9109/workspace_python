# 첫수를 넣으세요. 1Enter
# 끝수를 넣으세요. 5Enter
# 배수를 넣으세요. 2Enter
# 1에서부터 5까지의 2의 배수의 합은 6입니다.


a = input("첫수를 넣으세요")
b = input("끝수를 넣으세요")
c = input("배수를 넣으세요")

a1 = int(a)
b1 = int(b)
c1 = int(c)
sum = 0;

for i in range(a1, b1+1):
    if i % c1 == 0:
        sum += i

print("{}에서 부터 {}까지의 {}의 배수의 합은 {}입니다".format(a,b,c,sum))

