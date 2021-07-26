"""Lambda funksiya"""
"""def ikkilash(n):
    return n*2
print(ikkilash(4))"""
"""# lambda funksiyada kiritilgan sonning ikkilanganligini topish
ikkilash1=lambda a:a*2
print(ikkilash1(5))"""
"""# lambda funksiyada kiritilgan sonning kvadratini topish
ikkilash1=lambda a:a**2
print(ikkilash1(5))"""
"""# ikki va undan ortiq funksiya
def yigindi(a,b):
    return a+b
print(yigindi(2,3))"""
"""# ikki va undan ortiq lamda funksiya
yigindi1=lambda a,b:a+b
print(yigindi1(4,5))"""
def kvadrat(n):
    return lambda a:n**2
son=kvadrat(5)
print(son(2))
#print(kvadrat(5)(2))
