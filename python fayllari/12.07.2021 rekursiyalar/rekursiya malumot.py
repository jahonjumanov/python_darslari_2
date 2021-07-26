"""# qo'shish funksiya
a=1
b=2
def qoshish(a,b):
    return a+b
print(qoshish(a,b))"""
"""# Ayirish funksiya
a=5
b=2
def ayirish(a,b):
    return a-b
print(ayirish(a,b))"""
"""a=int(input("a="))
b=int(input("b="))
def qoshish(a,b):
    return a+b
def urta_arifmetig(a,b):
    return qoshish(a,b)/2
print(urta_arifmetig(a,b))"""
"""rekursiya ->o'ziga murojat qiladigan funksiya ekan"""
# n dan 1 gacha bo'lgan natural sonlarni teskari tartibda ekranga chiqarish
def birdanNgacha(n):
    if n==1:
        print(n)
    else:
        print(n)
        birdanNgacha(n-2)
birdanNgacha(5)




