# 2-masala. Uchburchakning tomonlari a=3,b=4,c=5
import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
P=a+b+c
p=(a+b+c)/2
S=int(math.sqrt(p*(p-a)*(p-b)*(p-c)))
print(f" Peremetri= {P} Yuzasi= {S}")