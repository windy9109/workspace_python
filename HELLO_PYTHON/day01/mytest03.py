#출력하고 싶은 단수를 입력하세요 6 Enter
#6*1=6
#.
#.

gogo = input("출력하고 싶은 단수를 입력하세요")
a = range(1,9+1)

for i in a:
    #print(gogo,"*",i,"=",i*int(gogo))
    print("{}*{}={}".format(gogo,i,int(gogo)*i))