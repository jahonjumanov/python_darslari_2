#5-masala
import math
x=int(input("x="))
y=int(input("y="))
a=int(input("a="))
G=(pow(math.cos(2*abs(y+x)-(x+y)),4*x*x))/(pow(math.atan(x+a),4)*pow(x,5))
print(G)
