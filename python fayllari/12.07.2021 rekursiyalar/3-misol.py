#3-misol .Faktarial
n=int(input("n="))
def fakt(n):
    if n==1 or n==0:
        return  1
    else:
        return n+fakt(n-1)
print(fakt(n))