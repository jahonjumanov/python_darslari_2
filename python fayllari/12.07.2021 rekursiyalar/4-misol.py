# 1 dan n gacha bo'lgan toq  natural sonlarni teskari tartibda ekranga chiqarish
n=int(input("n="))
def yigindi_toq(n):
    if n==1:
        print(n)
    else:
        if n%2==0:
            n=n-1
        print(n)
        yigindi_toq(n-2)
yigindi_toq(n)