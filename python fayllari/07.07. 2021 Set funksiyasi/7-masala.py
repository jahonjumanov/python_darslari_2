import random

a=[]
for i in range(10):
    b=random.randint(1,10)
    a.append(b)
a=set(a)
print(a)