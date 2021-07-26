# paralelopeped hajmini topish
import math
# 1-usul
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
def hajm(a,b):
    return lambda c:a*b*c
h=hajm(a,b)
print(h(c))

print("------------------------------------->")
# 2-usul
def hajm(a,b):
    return lambda c:a*b*c
h=hajm(2,3)
print(h(5))