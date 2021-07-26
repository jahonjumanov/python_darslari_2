#4-masala.
import math
y=int(input("a="))
h=int(input("b="))
A=(math.tan(pow(y,3)-pow(h,4))+pow(h,2))/(pow(math.sin(h),2)+y)
print(A)