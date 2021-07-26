# 3-masala. Sizga ikki tomoni bor va ular orasidagi burchak berilgan.
# Uchburchakning uchinchi tomoni toping
import math
a=int(input("a="))
b=int(input("b="))
x=int(input("burchak gradustini kiriting="))
burchak=x*math.pi/180
c=math.sqrt(a*a+b*b-2*a*b*math.cos(burchak))
print(f" c tomoni={c}")