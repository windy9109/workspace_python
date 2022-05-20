import random

def myrandom():
    b = random.random()
    if b>= 0.5: 
        return 1
    else: 
        return 0

rnd = myrandom()
print("rnd=",rnd)