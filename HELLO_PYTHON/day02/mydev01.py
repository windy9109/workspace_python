from dask.array.numpy_compat import divide
def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

sum = add(5,1)
min = minus(4,2)
mul = multiply(2,6)
div = divide(6,2)

print("sum", sum)
print("min", min)
print("mul", mul)
print("div", int(div))

