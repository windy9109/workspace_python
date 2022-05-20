from dask.array.numpy_compat import divide

def addminmuldiv(a,b):
    return a+b,a-b,a*b,a/b

#멀티리턴

#sum,min,mul,div = addminmuldiv(5,1)

#튜플: 배열인데 ()로 찍히는것, 작은배열과 동급
ammd = addminmuldiv(5,1)
print("ammd", ammd)

# print("sum", sum)
# print("min", min)
# print("mul", mul)
# print("div", int(div))

