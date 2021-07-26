#ikkita sonni yig'indisini n chi darajasini hisoblash
import math
# 1-usul
a=int(input("a="))
b=int(input("b="))
k=int(input("n="))
def daraja(a,b):
    return lambda n:(a+b)**n
n=daraja(a,b)
print(n(k))

print("----------------------------------------->")

# 2-usul
def daraja(a,b):
    return lambda n:(a+b)**n
n=daraja(2,3)
print(n(5))